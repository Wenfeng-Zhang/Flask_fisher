# -*- coding:utf-8 -*-

import threading
import time
from werkzeug.local import Local

# Flask里用字典保存线程数据
# 操作数据 werkzeug local Local 字典方式
# 线程的隔离 Local是一个重新封装的字典  用字典保存不同的ID号

# LocalStack、Local以及字典的关系和不同
# Local使用字典的方式实现的线程隔离
# LocalStack是线程隔离的栈结构
# 软件世界没有封装解决不了的问题，有就再封装一次
# 变成也是一种艺术 含蓄


class A(object):
    b = 1

my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    print('in new thread b is:' + str(my_obj.b))

new_t = threading.Thread(target=worker, name='zwf_thread')
new_t.start()
time.sleep(1)
# 主线程
print('in new thread b is:' + str(my_obj.b))



