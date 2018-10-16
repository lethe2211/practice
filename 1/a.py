# -*- coding: utf-8 -*-

import os
import sys

class Main(object):

    def __init__(self):
        pass

    def some_method(self):
        a, op, b = input().split()
        a = int(a)
        b = int(b)
        if op == '+':
            print(a + b)
        else:
            print(a - b)

        return None

if __name__ == '__main__':
    m = Main()
    m.some_method()
