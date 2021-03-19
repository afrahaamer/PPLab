#/usr/bin/env python        # 1 START UP LINE - Unix

"this is a test module"     # 2 MODULE DOCUMENTATION

import sys                  # 3 MODULE IMPORTS
import os

debug = True                # 4 GLOBAL VAR DECLARATION

class FooClass(object):     # 5 CLASS DECLARATION
    "Foo Class"
    pass

def test():                 # 6 FUNCTION DECLARATION
    "test function"
    foo = FooClass()

    if debug:
        print ('ran test()')

if __name__ == '__main__':  # 7 "MAIN" BODY
    test()