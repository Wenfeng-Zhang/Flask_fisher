# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String
from app.models.base import db, Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)              # 书名
    author = Column(String(30), default=u'未名')            # 作者
    binding = Column(String(20))                            # 装订的版本，精装还是平装
    publisher = Column(String(50))                          # 出版社
    price = Column(String(20))                              # 价格
    pages = Column(Integer)                                 # 页数
    pubdate = Column(String(20))                            # 出版年月
    isbn = Column(String(15), nullable=False, unique=True)  # isbn编号，unique不能有重复
    summary = Column(String(1000))                          # 书籍简介
    image = Column(String(50))                              # 图书的图片

    def sample(self):
        pass

