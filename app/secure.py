# -*- coding:utf-8 -*-
# secure主要是放数据库密码、账号、flask的app key，生产环境和开发环境不一样的参数 放到这里

DEBUG = True
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123456@127.0.0.1/fisher"
SECRET_KEY = '1234567989786546321'
# 这个文件不要上传到git

