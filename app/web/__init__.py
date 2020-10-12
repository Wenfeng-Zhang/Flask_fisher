# -*- coding:utf-8 -*-
from flask import Blueprint

# 可以设置静态文件夹和模板文件夹的路径
# web = Blueprint('web', __package__, template_folder='templates')  # type: #Blueprint
web = Blueprint('web', __package__)  # type: #Blueprint

from app.web import book
from app.web import user
