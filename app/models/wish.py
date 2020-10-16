# -*- coding:utf-8 -*-
from sqlalchemy.orm import relationship
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger, func, desc
from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 表示连接了User数据模型
    user = relationship('User')
    # 此处是将uid的值对应到user1模型的ID值上，也就是User数据模型的ID值对应.ForeignKey的意思是外键
    uid = Column(Integer, ForeignKey('user.id'))
    # book1 = relationship('Book')
    # bid = Column(Integer, ForeignKey('book1.id'))

    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)   # 将其设置为一个布尔模型，如果为True则为成功，否则失败

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        # 根据传入的一组isbn，到wish表中检索出相应的礼物，并计算出某个礼物的Wish心愿数量
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(
            Gift.isbn).all()
        count_list = [{'count': w[0], 'isbn':w[1]} for w in count_list]
        return count_list

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(
            desc(Wish.create_time)).all()
        return wishes

from app.models.gift import Gift