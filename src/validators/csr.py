class CSRValidator:
  @classmethod
  def valid(body: dict, field: str):
    valid = True
    message = 'Succesful operation'
    
    if not field in body.keys():
      valid = False
      message = f"'{field}' field is required"

    if body[field].strip() == '':
      valid = False
      message = f"'{field}' field cannot be empty"

    return {
      'valid': valid,
      'message': message
    }

  @classmethod
  def country(body: dict):
    valid = True
    message = 'Succesful operation'
    validation = CSRValidator.valid(body, 'username')

    if not validation['valid']:
      return validation

    country = body['country']

    if country != 'CU':
      valid = False
      message = 'Invalid country code'
    
    return {
      'valid': valid,
      'message': message
    }
  
  @classmethod
  def state(body: dict):
    valid = True
    message = 'Succesful operation'
    validation = CSRValidator.valid(body, 'state')

    if not validation['valid']:
      return validation
    
    return {
      'valid': valid,
      'message': message
    }

  @classmethod
  def organization_name(body: dict):
    valid = True
    message = 'Succesful operation'
    validation = CSRValidator.valid(body, 'organization_name')

    if not validation['valid']:
      return validation
    
    return {
      'valid': valid,
      'message': message
    }
  
  @classmethod
  def locality(body: dict):
    valid = True
    message = 'Succesful operation'
    validation = CSRValidator.valid(body, 'locality')

    if not validation['valid']:
      return validation
    
    return {
      'valid': valid,
      'message': message
    }
  
  @classmethod
  def common_name(body: dict):
    valid = True
    message = 'Succesful operation'
    validation = CSRValidator.valid(body, 'common_name')

    if not validation['valid']:
      return validation
    
    return {
      'valid': valid,
      'message': message
    }
