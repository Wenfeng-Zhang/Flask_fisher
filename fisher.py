# -*- coding:utf-8 -*-
from app import create_app

app = create_app()

# 打开调试模式
# host='0.0.0.0'表示可以接受外网输出 post='xxx'表示端口
# DEBUG必须都是大写才行，否则找不到。DEBUG在flask里面是个默认参数，默认值为False，所以在config文件里没有设置DEBUG也会有值
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
