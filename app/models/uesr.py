# -*- coding:utf-8 -*-
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)               #用户名
    phone_number = Column(String(18), unique=True)              #手机号
    _password = Column('password', String(128))
    email = Column(String(50), nullable=False, unique=True)     #email
    confirmed = Column(Boolean, default=False)                  #
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))                             #微信id
    wx_name = Column(String(32))                                #微信用户名

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
