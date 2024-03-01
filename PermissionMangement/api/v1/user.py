import logging
from flask_restful import Resource, request
from common.return_data import get_return_data, Success, Unsuccessfully
from PermissionMangement.models import User
from PermissionMangement.schemas import UserSchema
import json
_logger = logging.getLogger(__name__)


class UserViewSet(Resource):
    """
    Login View Class
    """
    def get(self):
        users = [
            {"name": "admin", "email": "admin.qq.com"},
            {"name": "god", "email": "god.qq.com"},
            {"name": "girl", "email": "girl.qq.com"},
            {"name": "boy", "email": "boy.qq.com"},
        ]
        return get_return_data(Success, users)
