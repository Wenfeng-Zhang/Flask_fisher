# -*- coding:utf-8 -*-
# 验证层
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp


class SearchForm(Form):
    # DataRequired是验证空格的
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


class DriftForm(Form):
    recipient_name = StringField(u'收件人姓名', validators=[DataRequired(), Length(
                                               min=2, max=20, message=u'收件人姓名长度必须在 2到20个字符之间')])
    mobile = StringField(validators=[DataRequired(), Regexp('^1[0-9]{10}$', 0, u'请输入正确的手机号')])
    message = StringField()
    address = StringField(validators=[DataRequired(), Length(min=10, max=70,
                                                             message=u'地址还不到10个字吗？尽量写详细一些吧')])