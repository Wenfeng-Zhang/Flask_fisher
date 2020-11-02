# -*- coding:utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, Integer, String, SmallInteger
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from contextlib import contextmanager
from time import time

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    '''
    重写filter_by，添加自己的规则
    '''

    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    # 将__abstract__设置为True，这样SQLAlchemy就不会将其视为表来创建了
    __abstract__ = True
    create_time = Column('create_time', Integer)
    # 根据更改这个小整数0或者1来表示当前行数据是否存在,0不存在1存在，也就是软删除，不是真正的物理删除
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(time())

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        self.status = 0
