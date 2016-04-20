# -*- coding: utf-8 -*-
'''
sys.exc_info
Catch the most recently handled exception.
'''

import sys
import traceback

def func(a, b):
    return a / b

if __name__ == '__main__':
    try:
        func(1, 0)
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        for filename, linenum, funcname, source in traceback.extract_tb(exc_tb):
            print "%-23s:%s '%s' in %s()" % (filename, linenum, source, funcname)
        print '=============='
        traceback.print_exc()







