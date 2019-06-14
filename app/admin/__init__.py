# -*- coding:utf-8 -*-
# 后端
# 开发人员 ： sunshenggang
# 开始时间 ： 19-6-13 下午4:17
# 开发工具 ： PyCharm Community Edition
from flask import Blueprint

admin = Blueprint('admin', __name__)

import app.admin.views