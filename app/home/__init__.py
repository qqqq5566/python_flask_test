# -*- coding:utf-8 -*-
#
# 开发人员 ： sunshenggang
# 开始时间 ： 19-6-13 下午4:23
# 开发工具 ： PyCharm Community Edition
from flask import Blueprint
home = Blueprint('home', __name__)

import app.home.views