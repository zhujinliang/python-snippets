# -*- coding: utf-8 -*-

import threading
from functools import wraps

local_context = threading.local()


def local_cache(name=None):
    """
    Decorate function to cache result in local_context.
    """
    def _local_cache(func):
        @wraps(func)
        def _cache(*args, **kwargs):
            local_name = name
            if local_name is None:
                local_name = 'func_' + func.__name__
            data = getattr(local_context, local_name, None)
            if data is None:
                data = func(*args, **kwargs)
                setattr(local_context, local_name, data)

            return data

        return _cache

    return _local_cache


@local_cache('data')
def get_data():
    import random
    return random.randrange(1, 100)

if __name__ == '__main__':
    d = get_data()
    print d
    d2 = get_data()
    print d2
