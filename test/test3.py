# -*- coding:utf-8 -*-

import threading
import time

def worker():
    print('i am thread')
    t = threading.current_thread()
    time.sleep(1)
    print(t.getName())

new_t = threading.Thread(target=worker, name='zwf_thread')
new_t.start()

t = threading.current_thread()
print(t.getName())


# 锁
# 细粒度的锁 程序员主动加的锁
# 粗粒度的锁 解释器锁 GIL 多核CPU 1个线程执行 一定程度上保证线程安全


# 用字典来表示并发的request请求
# 伪代码 request = {thread_key1:Request1, ....}
# thread_key1为 ID号
# 线程隔离



