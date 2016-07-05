#coding=utf-8

import functools, time


def time_decorato(func):
    """
    装饰器函数，输出运行时间
    """
    @functools.wraps(func)
    def wrapper(*args, **kw):
        local_time = time.time()
        func(*args, **kw)
        print('cost time : {:.2f}'.format(time.time() - local_time))
    return wrapper
