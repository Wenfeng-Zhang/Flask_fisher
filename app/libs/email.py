# -*- coding:utf-8 -*-
from threading import Thread
from flask import current_app, render_template
from app import mail
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            print(e)
            pass


def send_mail(to, subject, template, **kwargs):
    # msg = Message(u'测试邮件', sender='283721420@qq.com', body='Test', recipients=['283721420@qq.com'])
    msg = Message(u'[yushu]'+''+subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=['283721420@qq.com'])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()

