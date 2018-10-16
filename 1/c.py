# -*- coding: utf-8 -*-

import os
import sys

class Main(object):

    def __init__(self):
        pass

    def some_method(self):
        n = int(input())
        ts = list(map(int, input().split()))
        s = sum(ts)
        m = int(input())
        for i in range(m):
            p, x = map(int, input().split())
            print(s + (x - ts[p-1]))
        
        return None

if __name__ == '__main__':
    m = Main()
    m.some_method()
