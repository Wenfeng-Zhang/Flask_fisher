# -*- coding:utf-8 -*-
from flask import jsonify

from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

# 蓝图 bluepaint 蓝本,使用蓝图注册路由


# @web.route('/book/search/<q>/<page>')
# def login(q, page):
#     '''
#     q   :普通关键字、isbn
#     page：
#     :return:
#     '''
#     isbn_or_key = is_isbn_or_key(q)
#     if isbn_or_key == 'isbn':
#         result = YuShuBook.search_by_isbn(q)
#     else:
#         result = YuShuBook.search_by_keyword(q)
#     # 将返回的dict序列化
#     # API
#     return jsonify(result)