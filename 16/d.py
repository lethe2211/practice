import math

n, m = map(int, input().split())

# fixed = []
# for i in range(n):
#     fixed.append(list(map(int, input().split())))

# unfixed = []
# for i in range(m):
#     unfixed.append(list(map(int, input().split())))

xyrlist = []
for i in range(n + m):
    xyr = list(map(int, input().split()))
    if len(xyr) == 2:
        x, y = xyr
        r = -1
    else:
        x, y, r = xyr
    xyrlist.append((x, y, r))

ans = float("inf")
for i in range(len(xyrlist) - 1):
    for j in range(i + 1, len(xyrlist)):
        xi, yi, ri = xyrlist[i]
        xj, yj, rj = xyrlist[j]
        # print(xyrlist[i])
        # print(xyrlist[j])
        
        dist = math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
        # print(dist)
        if ri == -1 and rj == -1:
            ans = min(dist / 2, ans)
        elif ri == -1:
            ans = min(dist - rj, ans)
        elif rj == -1:
            ans = min(dist - ri, ans)
        else:
            ans = min(min(ri, rj), ans)
        # print(ans)
        # print()
print(ans)
    
