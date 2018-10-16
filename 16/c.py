n, t = map(int, input().split())
alist = map(int, input().split())

ans = 0
for a in alist:
    tmp = a
    while tmp < ans:
        tmp += t
    ans = tmp
print(ans)
