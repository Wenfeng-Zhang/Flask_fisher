# -*- coding:utf-8 -*-

def is_isbn_or_key(word):
    """
    返回判断是否是isbn书码
    :param word:得到的用户输入数据
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    shot_q = word.replace('-', '')
    if '-' in word and len(shot_q) == 10 and shot_q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
