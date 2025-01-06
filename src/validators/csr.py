class CSRValidator:
  @classmethod
  def _is_not_empty(cls, body: dict, field: str):
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
  def _exists(cls, body: dict, field):
    valid = True
    message = 'Successful operation'

    if field in body.keys():
      valid = False
      message = f"'{field}' field is required"

    
    return {
      'valid': valid,
      'message': message
    }

  @classmethod
  def validate(cls, body: dict, field):
    valid = True
    message = 'Successful operation'
    validation_empty = CSRValidator._is_not_empty(body, field)
    validation_exists = CSRValidator._exists(body, field)

    if not validation_empty['valid']:
      return validation_empty
    
    if not validation_exists['valid']:
      return validation_exists
    
    return {
      'valid': valid,
      'message': message
    }
