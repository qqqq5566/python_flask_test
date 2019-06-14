# -*- coding:utf-8 -*-
#
# 开发人员 ： sunshenggang
# 开始时间 ： 19-6-13 下午4:19
# 开发工具 ： PyCharm Community Edition
from flask import request, url_for, redirect, flash, g, session
from app import db
from . import admin

@admin.route('/')
def index():
    return '<h1>11</h1>'