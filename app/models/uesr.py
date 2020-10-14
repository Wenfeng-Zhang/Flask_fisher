# -*- coding:utf-8 -*-
from app import login_manager
from app.libs.helper import is_isbn_or_key
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)               # 用户名
    phone_number = Column(String(18), unique=True)              # 手机号
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), nullable=False, unique=True)     # email
    confirmed = Column(Boolean, default=False)                  #
    beans = Column(Float, default=0)                            # 虚拟货币数量
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))                             # 微信id
    wx_name = Column(String(32))                                # 微信用户名

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        # 密码对比
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 不允许一个用户同时赠送多本相同的图书
        # 一个用户不可能同时成为赠送者和索要者

        # 机不再赠送清单中，也不再心愿清单中才能添加
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn,  # 表示如果这本图书还没赠送出去就不能继续赠送
                                       launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))


