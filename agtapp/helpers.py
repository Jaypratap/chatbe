


def validateUserData(data):
    validate_data = {}
    validate_data['username'] = data['email']
    validate_data['password'] = data['password']
    validate_data['email'] = data['email']
    validate_data['phone_no'] = data['phone_no']
    validate_data['first_name'] = data['name']
    return validate_data