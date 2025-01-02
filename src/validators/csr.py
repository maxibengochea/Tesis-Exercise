class CSRValidator:
  @classmethod
  def _valid(cls, body: dict, field: str):
    valid = True
    message = 'Successful operation'

    if field in body.keys() and body[field].strip() == '':
      valid = False
      message = f"'{field}' field cannot be empty"

    return {
      'valid': valid,
      'message': message
    }

  @classmethod
  def country(cls, body: dict):
    valid = True
    message = 'Successful operation'
    validation = CSRValidator._valid(body, 'username')

    if not validation['valid']:
      return validation

    if 'country' in body.keys():
      country = body['country']

      if country != 'CU':
        valid = False
        message = 'Invalid country code'
    
    return {
      'valid': valid,
      'message': message
    }
  
  @classmethod
  def state(cls, body: dict):
    valid = True
    message = 'Successful operation'
    validation = CSRValidator._valid(body, 'state')

    if not validation['valid']:
      return validation
    
    return {
      'valid': valid,
      'message': message
    }

  @classmethod
  def organization_name(cls, body: dict):
    valid = True
    message = 'Successful operation'
    validation = CSRValidator._valid(body, 'organization_name')

    if not validation['valid']:
      return validation
    
    return {
      'valid': valid,
      'message': message
    }
  
  @classmethod
  def locality(cls, body: dict):
    valid = True
    message = 'Successful operation'
    validation = CSRValidator._valid(body, 'locality')

    if not validation['valid']:
      return validation
    
    return {
      'valid': valid,
      'message': message
    }
  
  @classmethod
  def common_name(cls, body: dict):
    valid = True
    message = 'Successful operation'
    validation = CSRValidator._valid(body, 'common_name')

    if not validation['valid']:
      return validation
    
    return {
      'valid': valid,
      'message': message
    }
