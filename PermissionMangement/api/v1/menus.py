import logging
from flask_restful import Resource, request
from common.return_data import get_return_data, Success, Unsuccessfully
from PermissionMangement.models import User
from PermissionMangement.schemas import UserSchema
import json

_logger = logging.getLogger(__name__)


class MenusViewSet(Resource):
    """
    Menus View Class
    """

    def get(self, role_id):
        menus = [
            {
                'label': '系统管理',
                'key': 'system',
                'icon': 'CalendarOutlined',
                'children': [
                    {
                        'label': '主页',
                        'key': 'main',
                        'icon': 'AppstoreOutlined',
                        'children': [],
                        'type': ''
                    },
                ],
                'type': ''
            },
            {
                'label': '用户管理',
                'key': 'users',
                'icon': 'AppstoreOutlined',
                'children': [
                    {
                        'label': '角色管理',
                        'key': 'roles',
                        'icon': 'AppstoreOutlined',
                        'children': [],
                        'type': ''
                    },
                ],
                'type': ''
            },
            {
                'label': '数据统计',
                'key': 'statistics',
                'icon': 'AppstoreOutlined',
                'children': [
                    {
                        'label': '指标统计',
                        'key': 'indicator',
                        'icon': '',
                        'children': [],
                        'type': ''
                    },
                    {
                        'label': '使用率统计',
                        'key': 'usage',
                        'icon': '',
                        'children': [],
                        'type': ''
                    },
                ],
                'type': ''
            },
            {
                'label': '页面管理',
                'key': 'pages',
                'icon': 'SettingOutlined',
                'children': [
                    {
                        'label': '动态路由',
                        'key': 'dynamic_route',
                        'icon': '',
                        'children': [],
                        'type': ''
                    },
                    {
                        'label': '动态页面',
                        'key': 'dynamic_page',
                        'icon': '',
                        'children': [],
                        'type': ''
                    },
                ],
                'type': ''
            }
        ]
        return get_return_data(Success, menus)

