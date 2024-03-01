#!/usr/bin/env python
# coding=utf-8

from flask_restful import Api
from flask import Blueprint
from PermissionMangement.api.common.version import ApiVersion

api_v2_bp = Blueprint('api_v2', __name__)
api_v2 = Api(api_v2_bp, catch_all_404s=True)
api_v2.add_resource(ApiVersion, "/version")

