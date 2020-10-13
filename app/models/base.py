# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, SmallInteger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    # 将__abstract__设置为True，这样SQLAlchemy就不会将其视为表来创建了
    __abstract__ = True
    create_time = Column('create_time', Integer)
    # 根据更改这个小整数0或者1来表示当前行数据是否存在,0不存在1存在，也就是软删除，不是真正的物理删除
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

