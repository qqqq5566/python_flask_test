# -*- coding:utf-8 -*-
#
# 开发人员 ： sunshenggang
# 开始时间 ： 19-6-13 下午4:53
# 开发工具 ： PyCharm Community Edition
from . import db
from datetime import datetime

class Terms(db.Model):
    __tablename__ = "terms"

    id = db.Column(db.Integer, primary_key=True)
    one = db.Column(db.String(100))
    two = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, default=datetime.now, index=True)

    def __repr__(self):
        return '<Term %r>' % self.name

