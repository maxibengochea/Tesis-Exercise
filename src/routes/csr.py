from src.blueprints import ca
from src.blueprints.csr import csr
from flask import request, jsonify
from src.validators.csr import CSRValidator
from src.client import Client

@csr.route('/issue_csr', methods=['GET'])
def issue_csr():
  #campos de la clase 'Client'
  fields = ['country', 'state', 'locality', 'organization_name', 'common_name']

  #capturar el body
  data = request.get_json(silent=True)
  body = data if data else {}
  new_body = {key: value for key, value in body.items() if key in fields}

  #validaciones
  validations = [CSRValidator.country(new_body), CSRValidator.locality(new_body), CSRValidator.state(new_body), 
                 CSRValidator.organization_name(body), CSRValidator.common_name(new_body)]
  
  for validation in validations:
    if not validation['valid']:
      return jsonify(validation)

  client = Client(**new_body)
  csr = client.issue_csr()
  ca.issue_certificate(csr)
  return jsonify({ 'message': 'CSR emited succesfully and certificate recived' })
