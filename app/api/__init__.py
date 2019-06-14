# -*- coding:utf-8 -*-
# API接口
# 开发人员 ： sunshenggang
# 开始时间 ： 19-6-13 下午4:21
# 开发工具 ： PyCharm Community Edition

from flask import Blueprint
api = Blueprint('api', __name__)

import app.api.views