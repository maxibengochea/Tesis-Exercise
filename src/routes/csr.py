from src.blueprints import ca
from src.blueprints.csr import csr
from flask import request, jsonify
from src.validators.csr import CSRValidator
from src.client import Client

@csr.route('/issue_csr', methods=['POST'])
def issue_csr():
  #capturar el body
  data = request.get_json()
  body = data if type(data) == dict else {}

  #validaciones
  validations = [CSRValidator.country(body), CSRValidator.locality(body), CSRValidator.state(body), 
                 CSRValidator.organization_name(body), CSRValidator.common_name(body)]
  
  for validation in validations:
    if not validation['valid']:
      return jsonify(validation)

  client = Client(body['country'], body['state'], body['locality'], body['organization_name'], body['common_name'])
  csr = client.issue_csr()
  return ca.issue_certificate(csr)


  



