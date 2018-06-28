from flask import g
from flask_httpauth import HTTPBasicAuth
from app.main.models import User
# from app.api.errors import error_response

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(email, password):
    user = User.get_user_by_email(email)
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)


@basic_auth.error_handler
def basic_auth_error():
    pass
    # return error_response(401)