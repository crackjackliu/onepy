#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    学习print函数的用法
"""

from functools import wraps


def pre_log(func):
    @wraps(func)
    def wrapper(*args, **kw):
        """wrapper wraps"""
        print('call %s（）:' % func.__name__)
        return func(*args, **kw)

    return wrapper


@pre_log
def hello(name):
    """hello func"""
    print('hello,%s' % name)


if __name__ == "__main__":
    hello('刘杰1')
    print(hello.__name__)
    print(hello.__doc__)
