# -*- coding:utf-8 -*-
# 验证层
from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email


class RegisterForm(Form):
    # DataRequired是验证空格的
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message=u'电子邮件不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message=u'密码不可以为空，请输入你的密码'), Length(6, 32)])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message=u'昵称至少需要两个字符，最多10个字符')])
