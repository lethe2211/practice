n, a, b = map(int, input().split())

ans = 0
for i in range(n):
    t = int(input())
    if (a <= t and t < b):
        continue
    else:
        ans += 1
print(ans)
