n = int(input())

m = (0, 0)
for i in range(n):
    a, b = map(int, input().split())
    if m[0] < a:
        m = (a, b)
print(m[0] + m[1])
    

