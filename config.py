# -*- coding:utf-8 -*-
#
# 开发人员 ： sunshenggang
# 开始时间 ： 19-6-13 下午5:25
# 开发工具 ： PyCharm Community Edition
import os

class Config:
    SECRET_KEY = 'mrsoft'
    SQLALCHEMY_TRACK_MODIFCATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Sun&*912687572@152.136.18.116:3306/youxi'
    DEBUG = True

config = {
    'default': DevelopmentConfig
}