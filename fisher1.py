# -*- coding:utf-8 -*-
from flask import Flask


app = Flask(__name__)
# 接受外部配置文件
app.config.from_object('config')




# @app.route('/hello/')
# def hello():
#     # 基于类的视图
#     # 视图函数还会返回status code 200,404,301等状态，
#     # 还会返回content-type http headers
#     # 如果不指定content-type的类型，默认是content-type = text/html
#     # 不单单是简单的函数返回
#     # Response
#
#     return 'hello, zwf'

# app.add_url_rule('/hello/', view_func=hello)


# 打开调试模式
# host='0.0.0.0'表示可以接受外网输出 post='xxx'表示端口
# DEBUG必须都是大写才行，否则找不到。DEBUG在flask里面是个默认参数，默认值为False，所以在config文件里没有设置DEBUG也会有值
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
