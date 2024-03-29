# -*- coding:utf-8 -*-

# urllib
# requests
import requests

class HTTP(object):
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # 是否返回json格式的数据
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
