# -*- coding:utf-8 -*-

from enum import Enum


class PendingStatus(Enum):
    Waiting = 1     # 等待
    Success = 2     # 成功
    Reject = 3      # 拒绝
    Redraw = 4      # 重置
