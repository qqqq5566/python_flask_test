# -*- coding:utf-8 -*-
#
# 开发人员 ： sunshenggang
# 开始时间 ： 19-6-13 下午4:12
# 开发工具 ： PyCharm Community Edition

from app import create_app, db
from app.models import *
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask import render_template, abort

app = create_app('default')
manage = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db)

manage.add_command('shell', Shell(make_context=make_shell_context))
manage.add_command('db', MigrateCommand)


@app.errorhandler(404)
def page_not_found(error):
    abort(404)

if __name__ == '__main__':
    app.run()