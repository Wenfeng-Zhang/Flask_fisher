# -*- coding:utf-8 -*-
from flask import current_app, render_template
from app import mail
from flask_mail import Message


def send_mail(to, subject, template, **kwargs):
    # msg = Message(u'测试邮件', sender='283721420@qq.com', body='Test', recipients=['283721420@qq.com'])
    msg = Message(u'[yushu]'+''+subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=['283721420@qq.com'])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)




