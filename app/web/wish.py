# -*- coding:utf-8 -*-
from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from app import db
from app.libs.email import send_mail
from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.trade import MyTrades
from app.view_models.wish import MyWishes
from app.web import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    uid = current_user.id
    wished_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wished_of_mine]
    gift_count_list = Wish.get_gifts_counts(isbn_list)
    view_model = MyTrades(wished_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.trades)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        # 事务，保证数据一致性
        # 回滚 rollback
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash(u'这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
@login_required
def satisfy_wish(wid):
    wish = Wish.query.get_or_404(wid)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        flash(u'你还没有上传此书，'
              u'请点击“加入到赠送清单”添加此书。添加前，请确保自己可以赠送此书')
    else:
        send_mail(wish.user.email,
                   u'有人想送你一本书', 'email/satisify_wish.html', wish=wish, gift=gift)
        flash(u'已向他/她发送了一封邮件，如果他/她愿意接受你的赠送，你将收到一个鱼漂')
    return redirect(url_for('web.book_detail', isbn=wish.isbn))


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn=isbn, launched=False).first_or_404()
    with db.auto_commit():
        wish.delete()
    return redirect(url_for('web.my_wish'))

