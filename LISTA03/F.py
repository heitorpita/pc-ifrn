c, q = map(int, (input().split()))
 
if c == 1:
    c = 4 * q
elif c == 2:
     c = 4.50 * q
elif c == 3:
     c = 5 * q
elif c == 4:
    c = 2 * q
elif c == 5:
     l = 1.50 * q 
print(f"Total: R$ {c:.2f}")