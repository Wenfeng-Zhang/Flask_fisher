# -*- coding:utf-8 -*-

class MyResource(object):
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('process exception')
        else:
            print('no exception')
        # 如果是False，会在外面的with之后继续抛出异常，如果为True，意思是用户内部已经处理了，则不会抛出
        # 如果什么都不返回，就默认是None，在python里也是False的意思，相当于返回的是False
        return False

    def query(self):
        print('query data')

# try:
#     with MyResource() as resource:
#         1/0
#         resource.query()
# except Exception as e:
#     pass

print [None] + list(None or ())

# for i in [None]:
#     print i



