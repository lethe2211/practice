from collections import Counter

n, k = map(int, input().split())

cnt = Counter()
for i in range(n):
    p = input()[0]
    cnt[p] += 1
print(list(reversed(sorted(list(cnt.values())))))

l = list(reversed(sorted(list(cnt.values()))))

ans = 0
for i in range(len(l)):
    c = 0
    flg = False
    for j in range(len(l)):
        if l[j] != 0:
            flg = True
        if l[j] > 0 and c < k:
            l[j] -= 1
            c += 1
        print(l)
    ans += 1
    if flg == False:
        break
print(ans)
