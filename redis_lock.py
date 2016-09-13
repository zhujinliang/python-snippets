# -*- coding: utf-8 -*-

from xxx import redis


__all__ = [
    'acquire_lock',
    'release_lock',
]


def acquire_lock(lock_key, time=600):
    '''
    Acquire lock.
    若lock不存在即当前状态为unlock，则获取到，返回True
    若lock存在即当前状态为locked，则未获取到，返回False
    '''
    lock = redis.setnx(lock_key, 1)
    if lock:
        redis.expire(lock_key, time)
    return lock


def release_lock(lock_key):
    '''
    Release lock.
    将lock状态改为unlock
    '''
    redis.delete(lock_key)
