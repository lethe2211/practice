s = input()
t = input()

s_sorted = ''.join(sorted(list(s)))
t_sorted = ''.join(reversed(sorted(list(t))))

if s_sorted < t_sorted:
    print('Yes')
else:
    print('No')
    
