n = int(input())
ablist = [list(map(int, input().split())) for i in range(n)]
cdlist = [list(map(int, input().split())) for i in range(n)]
ablist.sort()
cdlist.sort()

abflag = [False for i in range(n)]
cdflag = [False for i in range(n)]

for i in range(n - 1, -1, -1):
    candidate = (-1, -1)
    c_index = None
    for j in range(n - 1, -1, -1):
        print(cdlist[i])
        print(ablist[j])

        if abflag[j] or cdflag[i]:
            continue
        
        a, b = ablist[j]
        c, d = cdlist[i]
        if a < c and b < d:
            if candidate[1] < b:
                candidate = (a, b)
                c_index = j
                print(candidate)
                print(c_index)
        print()
    if not (candidate == (-1, -1)):
        abflag[c_index] = True
        cdflag[i] = True

# print(abflag)
# print(cdflag)

print(len([flag for flag in abflag if flag == True]))
