import sys

s = input()

if s.find('N') != -1:
    if s.find('S') == -1:
        print('No')
        sys.exit()

if s.find('S') != -1:
    if s.find('N') == -1:
        print('No')
        sys.exit()

if s.find('W') != -1:
    if s.find('E') == -1:
        print('No')
        sys.exit()

if s.find('E') != -1:
    if s.find('W') == -1:
        print('No')
        sys.exit()
        
print('Yes')
