# -*- coding:utf-8 -*-
from flask import Blueprint, render_template

# 可以设置静态文件夹和模板文件夹的路径
# web = Blueprint('web', __package__, template_folder='templates')  # type: #Blueprint
web = Blueprint('web', __package__)  # type: #Blueprint


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


from app.web import main
from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import wish
