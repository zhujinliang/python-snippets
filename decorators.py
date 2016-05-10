# -*- coding: utf-8 -*-

import threading

from functools import wraps


# function decorator
def login_required(func):
    '''
    Verify the user when request a page.
    '''
    @wraps(func)
    def _verify_login(*args, **kwargs):
        # verify user
        pass
        return func(*args, **kwargs)

    return _verify_login

'''
Example:
@login_required
def get_user_info(*args, **kwargs):
    pass

get_user_info = login_required(get_user_info)(*args, **kwargs)
'''



# function decorator with parameters
def redirect(url):
    print 'Redirect to %s' % url

user_login = True


def login_required(url='/login'):
    '''
    Verify the user when request a page.
    If user is not login, redirect to login page.
    '''
    @wraps(func)
    def wrapper(func):
        def _verify_login(*args, **kwargs):
            # verify user login
            if user_login:
                return func(*args, **kwargs)
            else:
                return redirect(url)
        return _verify_login

    return wrapper
'''
Example:
@login_required(url='/user/login')
def get_user_info(*args, **kwargs):
    pass

get_user_info = login_required(url='/user/login')(get_user_info)(*args, **kwargs)
'''


# class decorator
class async(object):
    ''' Decorator that turns a callable function into a thread.'''
    __name__ = 'async'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        thread = threading.Thread(
            target=self.func,
            args=args,
            kwargs=kwargs
        )
        thread.start()
        return True


'''
Example:
@async
def send_mail(*args, **kwargs):
    pass


send_mail = async(send_mail)(*args, **kwargs)
'''