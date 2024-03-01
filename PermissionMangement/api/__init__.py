#!/usr/bin/env python
# coding=utf-8

from .v1 import api_v1_bp
from .v2 import api_v2_bp
from .common import api_common_bp

# ------------------------------
# API配置
# ------------------------------

# 允许访问的API版本
VERSIONS_ALLOWED = ['v1', 'v2', 'api_common']

# API版本映射
API_VERSION_MAPPING = {
    'v1': api_v1_bp,
    'v2': api_v2_bp,
    'api_common': api_common_bp
}

# 注册自定义蓝图
APP_BLUEPRINTS = [
    'common:common_bp',
]
