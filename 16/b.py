n = int(input())
d, x = map(int, input().split())

alist = [int(input()) for i in range(n)]

ans = x

for a in alist:
    if d % a == 0:
        ans += (d // a)
    else:
        ans += (d // a) + 1

print(ans)
