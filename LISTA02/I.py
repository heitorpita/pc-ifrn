l, d = map(int, input().split())
k, p = map(int, input().split())
total = (l // d) * p + l * k
print(total)