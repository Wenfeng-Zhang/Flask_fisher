# -*- coding:utf-8 -*-
from flask import current_app, flash
from flask_login import login_required, current_user
from app.models.base import db
from app.models.gift import Gift
from app.web import web


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # 事务，保证数据一致性
        # 回滚 rollback
        try:
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            # 如果上面执行失败了回滚数据库
            db.session.rollback()
    else:
        flash(u'这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass


