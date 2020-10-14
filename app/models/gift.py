# -*- coding:utf-8 -*-
from sqlalchemy.orm import relationship
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 表示连接了User数据模型
    user1 = relationship('User')
    # 此处是将uid的值对应到user模型的ID值上，也就是User数据模型的ID值对应.ForeignKey的意思是外键
    uid = Column(Integer, ForeignKey('user1.id'))
    # book1 = relationship('Book')
    # bid = Column(Integer, ForeignKey('book1.id'))

    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)   # 将其设置为一个布尔模型，如果为True则为成功，否则失败



