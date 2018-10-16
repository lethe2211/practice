import os
import sys
import math

def func(h, w, ans):
    for i in range(1, w + 1):
        first = h * i

        if (w - i) % 2 == 0:
            second = h * ((w - i) // 2)
            s = abs(first - second)
            ans = min(s, ans)
        else:
            second = h * ((w - i) // 2)
            third = h * (w - i - (w - i) // 2)
            s = max(abs(first - second), abs(second - third), abs(third - first))
            ans = min(s, ans)

        if h % 2 == 0:
            second = (h // 2) * (w - i)
            s = abs(first - second)
            ans = min(s, ans)
        else:
            second = (h // 2) * (w - i)
            third = (h - (h // 2)) * (w - i)
            s = max(abs(first - second), abs(second - third), abs(third - first))
            ans = min(s, ans)
    return ans

h, w = map(int, input().split())

if h % 3 == 0 or w % 3 == 0:
    print(0)
    exit()

ans = float('inf')

ans = func(h, w, ans)
ans = func(w, h, ans)
    
print(ans)
