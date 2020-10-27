# -*- coding:utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from . import web
from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.models.uesr import User, db
from flask_login import login_user, logout_user
from app.libs.email import send_mail


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)  # 持续性cookie，免登陆
            next = request.args.get('next')   # 获取到url地址中next之后的
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash(u'账号不存在或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()  # 利用first_or_404不会报错，会跳到一个Not Found页面
            send_mail(form.email.data, u'重置你的密码',
                      'email/reset_password.html', user=user,
                      token=user.generate_token())
            flash(u'一封邮件已发送到邮箱' + account_email + u', 请及时查收')
            # return redirect(url_for('web.login'))
    return render_template('auth/forget_password_request.html', form=form)

# 单元测试


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        success = User.reset_password(token, form.password1.data)
        if success:
            flash(u'你的密码已更新，请使用新密码登录')
            return redirect(url_for('web.login'))
        else:
            flash(u'密码重置失败')
    return render_template('auth/forget_password.html', form=form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
