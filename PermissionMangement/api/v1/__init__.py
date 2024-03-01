from flask_restful import Api
from flask import Blueprint

from .login import LoginViewSet
from .user import UserViewSet
from PermissionMangement.api.common.version import ApiVersion

api_v1_bp = Blueprint("api_v1", __name__)
api_v1 = Api(api_v1_bp, catch_all_404s=True)
api_v1.add_resource(ApiVersion, "/version")
api_v1.add_resource(LoginViewSet, "/login")
api_v1.add_resource(UserViewSet, "/users")
