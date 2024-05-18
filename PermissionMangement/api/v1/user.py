import logging
from flask_restful import Resource, request
from common.return_data import get_return_data, Success, Unsuccessfully
from PermissionMangement.models import User
from PermissionMangement.schemas import UserSchema
import json

_logger = logging.getLogger(__name__)


class UsersViewSet(Resource):
    """
    Login View Class
    """

    def get(self):
        users = [
            {"key": 1, "name": "丁先生", "age": 23, "address": "北京市"},
            {"key": 2, "name": "王女士", "age": 22, "address": "天津市"},
            {"key": 3, "name": "胡先生", "age": 21, "address": "重庆市"},
            {"key": 4, "name": "李先生", "age": 20, "address": "上海市"},
        ]
        return get_return_data(Success, users)


class UserViewSet(Resource):
    """
    Login View Class
    """

    def get(self, id):
        user = {
            "key": 1,
            "name": "admin",
            "age": 23,
            "address": "北京市",
            "role_id": 1,
        }
        return get_return_data(Success, user)
