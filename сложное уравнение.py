import sys

a = input('a = ')
if a.lstrip('-').isdigit():
    a = int(a)
else:
    sys.exit()
b = input('b = ')
if b.lstrip('-').isdigit():
    b = int(b)
else:
    sys.exit()
c = input('c = ')
if c.lstrip('-').isdigit():
    c = int(c)
else:
    sys.exit()
d = input('d = ')
if d.lstrip('-').isdigit():
    d = int(d)
else:
    sys.exit()
if c != 0 and -d / c == 0:
    print("NO")
if a == 0 and b != 0:
    print("NO")
if a != 0 and c != 0 and -d / c == -b / a:
    print('NO')
if a != 0 and -b / a != int(-b / a):
    print("NO")
elif a == 0 and b == 0:
    print('INF')
else:
    x = -b / a
    print(f'x = {int(x)}')