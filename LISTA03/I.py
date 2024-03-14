d = int(input())
a, l, p = map(int, input().split())

if d <= min(a, l,p):
    print('S')
else:
    print('N')