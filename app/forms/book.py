# -*- coding:utf-8 -*-
# 验证层
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired
class SearchForm(Form):
    # DataRequired是验证空格的
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


