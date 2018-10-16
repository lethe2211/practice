n = int(input())

alist = [a for a in map(int, input().split())]
blist = [b for b in map(int, input().split())]
flags = [False for _ in range(n)]

for i in range(n):
    if alist[i] == blist[i]:
        flags[i] = True

i = 0
while i < n:
    tempa = alist[i]
    tempb = blist[i]

    newi = i + 1
    while newi < n - 1 and flags[newi] == True:
        newi += 1
    if newi >= n:
        break
        
    if alist[i] > blist[i]:
        alist[newi] += 2 * (tempa - tempb)
        blist[i] += tempa - tempb
    elif alist[i] < blist[i]:
        if (blist[i] - alist[i]) % 2 == 0:
            alist[i] += tempb - tempa
            blist[newi] += (tempb - tempa) // 2
        else:
            alist[i] = tempb + 1
            blist[i] = tempb + 1
            alist[newi] += 2
            blist[newi] += ((tempb - tempa) // 2) + 1
    i = newi
    print(alist)
    print(blist)
    print()
    
    # while not (alist[i] == blist[i]):
    #     if alist[i] > blist[i]:
    #         alist[newi] += 2
    #         blist[i] += 1
    #     elif alist[i] < blist[i]:
    #         alist[i] += 2
    #         blist[newi] += 1

if alist[-1] == blist[-1]:
    print('Yes')
else:
    print('No')
