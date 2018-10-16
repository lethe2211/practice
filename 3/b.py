a, b, c = map(int, input().split())

for i in range(1, a + 2):
    if (b * i + c) % a == 0:
        print('YES')
        break
else:
    print('NO')
