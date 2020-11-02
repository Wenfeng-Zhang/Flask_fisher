# -*- coding:utf-8 -*-

from enum import Enum


class PendingStatus(Enum):
    Waiting = 1     # 等待
    Success = 2     # 成功
    Reject = 3      # 拒绝
    Redraw = 4      # 重置

    @classmethod
    def pending_str(cls, status, key):
        key_map = {
            cls.Waiting: {
                        'requester': u'等待对方邮寄',
                        'gifter': u'等待你邮寄'
                        },
            cls.Success: {
                        'requester': u'对方已邮寄',
                        'gifter': u'你已邮寄'
                        },
            cls.Reject: {
                        'requester': u'对方已拒绝',
                        'gifter': u'你已拒绝'
                        },
            cls.Redraw: {
                        'requester': u'对方已撤销',
                        'gifter': u'你已撤销'
                        },
        }
        return key_map[status][key]
