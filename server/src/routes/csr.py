from src.routes import ca
from flask import request, jsonify
from src.validators.csr import CSRValidator
from src.client import Client
from flask import Blueprint
from src.quorum import Quorum

csr = Blueprint('csr', __name__)

@csr.route('/issue_csr', methods=['POST'])
def issue_csr():
  #campos de la clase 'Client'
  fields = ['organization_name', 'common_name']

  #capturar el body
  data = request.get_json(silent=True)
  body = data if data else {}
  new_body = {key: value for key, value in body.items() if key in fields}

  #validaciones
  validations = [CSRValidator.validate(new_body, 'organization_name'), CSRValidator.validate(new_body, 'common_name')]
  
  for validation in validations:
    if not validation['valid']:
      return jsonify(validation)

  client = Client(**new_body)
  csr = client.issue_csr()
  Quorum.config_start_node(new_body['common_name'])
  
  if not ca.issue_certificate(csr):
    return jsonify({ 
      'valid': False,
      'message': 'CSR already emited' 
    })
  
  return jsonify({
    'valid': True,
    'message': 'CSR emited succesfully and certificate recived' 
  })
