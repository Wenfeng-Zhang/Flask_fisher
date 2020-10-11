# -*- coding:utf-8 -*-

import threading
import time

from werkzeug.local import LocalStack

def a():
    print(1)

s = LocalStack()
s.push(99)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)



