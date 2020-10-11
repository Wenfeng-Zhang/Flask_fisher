# -*- coding:utf-8 -*-
from flask import Blueprint

web = Blueprint('web', __package__)  # type: #Blueprint

from app.web import book
from app.web import user
