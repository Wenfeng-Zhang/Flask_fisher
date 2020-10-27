# -*- coding:utf-8 -*-
from flask import flash, redirect, url_for
from . import web
from flask_login import login_required, current_user
from app.models.gift import Gift


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    current_gift = Gift.query.get_or_404(gid)
    if current_gift.is_yourself_gift(current_user.id):
        flash(u'这本书是你自己的，不能向自己索要书籍哦')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    pass


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
