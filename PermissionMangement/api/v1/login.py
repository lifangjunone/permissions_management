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
                "token": create_access_token(identity=username),
                "vertical_menu": [
                    {
                        "key": "1",
                        "icon": "&#xe62d;",
                        "label": "Dashboard",
                        "title": "Dashboard"
                    },
                    {
                        "key": "2",
                        "icon": "&#xe635;",
                        "label": "Authrization",
                        "title": "Authrization",
                        "children": [
                            {
                                "icon": "&#xe63d;",
                                "key": "3",
                                "label": "User",
                                "title": "User"
                            },
                            {
                                "icon": "&#xe64d;",
                                "key": "4",
                                "label": "Role",
                                "title": "Role"
                            },
                            {
                                "icon": "&#xeb68;",
                                "key": "5",
                                "label": "Permissions",
                                "title": "Permissions"
                            }
                        ]
                    },
                    {
                        "key": "6",
                        "icon": "&#xe667;",
                        "label": "System",
                        "title": "System",
                        "children": [
                            {
                                "icon": "&#xe6e8;",
                                "key": "7",
                                "label": "View Manage",
                                "title": "View Manage"
                            },
                            {
                                "icon": "&#xe6ce;",
                                "key": "8",
                                "label": "API Manage",
                                "title": "API Manage"
                            }
                        ]
                    },
                    {
                        "key": "9",
                        "icon": "&#xe63f;",
                        "label": "Logging",
                        "title": "Logging",
                        "children": [
                            {
                                "icon": "&#xe616;",
                                "key": "10",
                                "label": "Login Log",
                                "title": "Login Log"
                            },
                            {
                                "icon": "&#xe664;",
                                "key": "11",
                                "label": "Operate Log",
                                "title": "Operate Log"
                            }
                        ]
                    }
                ],
                "horizontal_menu": [
                    {
                        "key": "Manual",
                        "icon": "&#xe600;",
                        "label": "Manual",
                        "href": "http://www.baidu.com",
                        "title": "Manual"
                    },
                    {
                        "key": "Email",
                        "icon": "&#xe622;",
                        "label": "Email",
                        "title": "Email"
                    },
                    {
                        "key": "Message",
                        "icon": "&#xe612;",
                        "label": "Message",
                        "title": "Message"
                    },
                    {
                        "key": "User",
                        "url": "src/assets/images/avatar.jpg",
                        "label": "User",
                        "title": "User",
                        "children": [
                            {
                                "icon": "&#xe641;",
                                "key": "Your profile",
                                "title": "Your profile",
                                "label": "Your profile"
                            },
                            {
                                "icon": "&#xe718;",
                                "key": "Modify password",
                                "title": "Modify password",
                                "label": "Modify password"
                            },
                            {
                                "icon": "&#xe648;",
                                "key": "Setting",
                                "title": "Setting",
                                "label": "Setting"
                            },
                            {
                                "icon": "&#xe647;",
                                "key": "Sign out",
                                "title": "Sign out",
                                "label": "Sign out"
                            }
                        ]
                    }
                ]
            }
            return get_return_data(Success, data)
        else:
            return get_return_data(Unsuccessfully, {}, msg="账号或者密码错误")
