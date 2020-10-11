# -*- coding:utf-8 -*-
from flask import jsonify, request
from app.forms.book import SearchForm
from app.web import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

# 蓝图 bluepaint 蓝本,使用蓝图注册路由

# 全局app对象因为在主线程所以只有一个，但是app上下文在子线程所以可能有多个，当多个用户共享同一个信息的时候可以将信息放在app对象里
@web.route('/test')
def test1():
    import app
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = '2'
    print('--------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', '2')
    print('--------------')
    print(id(app))
    return ''

@web.route('/book/search/')
def search():
    '''
    q   :普通关键字、isbn
    page：
    :return:
    '''
    # Request
    # Request几乎包含所有的HTTP信息。查询参数、POST参数、remote ip

    # # 至少一个字符，长度限制
    # q = request.args['q']
    # # 正整数，也要有一个最大值的限制
    # page = request.args['page']
    # # 将不可变的字典转换成可变字典
    # # a = request.args.to_dict()

    # 验证层
    form = SearchForm(request.args)
    #如果通过验证则符合要求
    if form.validate():
        # 因为form里有默认值，所以要从form里取
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        # 将返回的dict序列化
        # API
        return jsonify(result)
    else:
        return jsonify(form.errors)
