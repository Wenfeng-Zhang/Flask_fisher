# -*- coding:utf-8 -*-
from flask import current_app
from sqlalchemy.orm import relationship
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, desc, func
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 表示连接了User数据模型
    user = relationship('User')
    # 此处是将uid的值对应到user模型的ID值上，也就是User数据模型的ID值对应.ForeignKey的意思是外键
    uid = Column(Integer, ForeignKey('user.id'))
    # book1 = relationship('Book')
    # bid = Column(Integer, ForeignKey('book1.id'))

    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)   # 将其设置为一个布尔模型，如果为True则为成功，否则失败

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from app.models.wish import Wish
        # 根据传入的一组isbn，到wish表中检索出相应的礼物，并计算出某个礼物的Wish心愿数量
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False,
                                                                             Wish.isbn.in_(isbn_list),
                                                                             Wish.status == 1
                                                                             ).group_by(Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn':w[1]} for w in count_list]
        return count_list

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 对象代表一个礼物，是具体的对象
    # 类代表礼物这个事物，它是抽象，不是具体的“一个”
    @classmethod
    def recent(cls):
        # 链式调用
        # 主题 query
        # 子函数

        # 先以isbn来进行group_by分组然后用distinct()去重，再进行时间order_by排序，用limit进行显示数量限制
        # recent_gift = Gift.query.filter_by(
        #     launched=False).group_by(
        #     Gift.isbn).limit(
        #     current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        # recent_gift = Gift.query.with_entities(
        #     Gift.isbn).filter_by(
        #     launched=False).order_by(
        #     desc(Gift.create_time)).limit(
        #     current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        # print recent_gift, 'type', type(recent_gift)
        # return recent_gift

        # recent_gift = Gift.query.filter_by(
        #     launched=False).order_by(
        #     desc(Gift.create_time)).limit(
        #     current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        # return recent_gift

        # recent_gift = Gift.query.filter_by(
        #     launched=False).distinct(Gift.isbn).all()

        # recent_gift = Gift.query.filter_by(
        #     launched=False).distinct(Gift.isbn).all()

        # 因为mysql和postgresql的group by不同，postgresql需要聚合以后再查询，所以另一种方式是先得到去重后的数据，
        # 再用子查询得到和原表中ID相同的数据并进行排序等操作，这样就相当于省去group by的操作
        recent_gift = Gift.query.filter_by(
            launched=False).distinct(Gift.isbn).subquery()

        recent_gift = Gift.query.filter_by(
            id=recent_gift.c.id).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).all()

        return recent_gift
