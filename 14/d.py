l = int(input())
s = input()
t = input()

if (s[0] > t[0]):
    tmp = s
    s = t
    t = tmp

if ((s[0] == t[0]) and (s[-1] > t[-1])):
    tmp = s
    s = t
    t = tmp

if ((s[0] == t[0]) and (s[-1] == t[-1]) and (s.find(t) == -1 or t.find(s) == -1)):
    tmp = s
    s = t
    t = tmp

if ((s[0] == t[0]) and (s[-1] == t[-1]) and (s.find(t) != -1 and t.find(s) != -1) and s > t):
    tmp = s
    s = t
    t = tmp
    
s_cnt = 0
t_cnt = 0

ltmp = l
while (not (ltmp % len(s) == 0)):
    # print(ltmp)
    ltmp -= len(t)
    t_cnt += 1

s_cnt = ltmp // len(s)

# print(s_cnt)
# print(t_cnt)

ans = ''
for i in range(s_cnt):
    ans += s
for i in range(t_cnt):
    ans += t
print(ans)
