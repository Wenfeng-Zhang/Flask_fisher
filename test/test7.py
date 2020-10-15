# -*- coding:utf-8 -*-

# 以线程ID号作为key的 字典 -> Local -> LocalStack

# AppContext RequestContext -> LocalStack

# Flask -> AppContext    Request -> RequestContext

# current_app -> (LocalStack.top = AppContext    top.app = Flask)

# request -> (LocalStack.top = RequestContext    top.request = Request)


from contextlib import contextmanager
from datetime import datetime


class A(object):

    def run(self):
        print('aaaa')

@contextmanager
def a():
    print('1111111111')
    yield A()
    print('2222222222')

# with a() as r:
#     r.run()



print(int(datetime.now().timestamp()))












