# -*- coding:utf-8 -*-
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app

    # 第二种方案
    # with app.app_context():
    #     db.create_all()

    # 第三种是直接在SQLAlchemy的对象里传入app，也就是db = SQLAlchemy(app)，这里不推荐使用这种方法

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
