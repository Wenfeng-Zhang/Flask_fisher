# -*- coding:utf-8 -*-
# 验证层
from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError, EqualTo
from app.models.uesr import User


class RegisterForm(Form):
    # DataRequired是验证空格的
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message=u'电子邮件不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message=u'密码不可以为空，请输入你的密码'), Length(6, 32)])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message=u'昵称至少需要两个字符，最多10个字符')])

    # 邮箱校验，validate_xxx是固定格式，xxx如果和上面的某个属性同名，会自动识别检测这个属性
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'昵称已存在')


class LoginForm(Form):
    # DataRequired是验证空格的
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message=u'电子邮件不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message=u'密码不可以为空，请输入你的密码'), Length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message=u'电子邮件不符合规范')])


class ResetPasswordForm(Form):
    '''
    密码与新密码校验
    '''
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message=u'密码长度至少需要在6到32个字符之间'),
        EqualTo('password2', message=u'两次输入的密码不相同')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)
    ])

