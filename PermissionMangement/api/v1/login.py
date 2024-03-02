import logging
from flask_restful import Resource, request
from common.return_data import get_return_data, Success, Unsuccessfully
from flask_jwt_extended import create_access_token
import json
_logger = logging.getLogger(__name__)


class LoginViewSet(Resource):
    """
    Login View Class
    """
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if username == "admin" and password == "123456":
            data = {
                "token": create_access_token(identity=username)
            }
            return get_return_data(Success, data)
        else:
            return get_return_data(Unsuccessfully, {}, msg="账号或者密码错误")
