import logging
from flask_restful import Resource, request
from common.return_data import get_return_data, Success, Unsuccessfully
from PermissionMangement.models import User
from PermissionMangement.schemas import UserSchema
import json
_logger = logging.getLogger(__name__)


class LoginViewSet(Resource):
    """
    Login View Class
    """
    def post(self):
        data = json.loads(request.get_data().decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        if username == "admin" and password == "123456":
            users = [
                {"name": "admin", "email": "admin.qq.com"},
                {"name": "god", "email": "god.qq.com"},
                {"name": "girl", "email": "girl.qq.com"},
                {"name": "boy", "email": "boy.qq.com"},
            ]
            return get_return_data(Success, users)
        else:
            return get_return_data(Unsuccessfully, {}, msg="账号或者密码错误")
