# -*- coding: utf-8 -*-

import os
import sys

class Main(object):

    def __init__(self):
        pass

    def some_method(self):
        a, b, c, d = map(int, input().split())
        one = a * b
        another = c * d
        print(max(one, another))
        return None

if __name__ == '__main__':
    m = Main()
    m.some_method()
