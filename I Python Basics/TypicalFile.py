"DOCUMENTATION"

import os
import sys 

globalVar = 10

class classDeclaration(object):
    "CLASS"
    pass

def test():
    "test function"
    foo = classDeclaration()
    if globalVar:
        print("ran test()")

if __name__ == '__main__':
    test()      