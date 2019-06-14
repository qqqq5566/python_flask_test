# -*- coding:utf-8 -*-
#
# 开发人员 ： sunshenggang
# 开始时间 ： 19-6-13 下午4:11
# 开发工具 ： PyCharm Community Edition
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)

    #添加配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #注册数据库
    db.init_app(app)

    #注册蓝图
    from app.admin import admin as admin_blueprint
    from app.home import home as home_blueprint
    from app.api import api as api_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app