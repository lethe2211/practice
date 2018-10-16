from collections import Counter
import itertools
import math

n, p = map(int, input().split())
alist = map(int, input().split())

d = Counter()
for a in alist:
    d[a % 2] += 1

# print(d)

zeros = 2 ** d[0]


ones = 0
if p == 0:
    for i in range(d[1]+1):
        if i % 2 == 0:
            ones += math.factorial(d[1]) // (math.factorial(d[1] - i) * math.factorial(i))
        # print(i)
        # print(ones)
else:
    for i in range(d[1]+1):
        if i % 2 == 1:
            ones += math.factorial(d[1]) // (math.factorial(d[1] - i) * math.factorial(i))
        # print(i)
        # print(ones)

# print(zeros)
# print(ones)

print(zeros * ones)
