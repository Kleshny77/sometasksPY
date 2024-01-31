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
while a > b:
    if a % 2 == 0 and a // 2 >= b:
        a //= 2
        print(':2')
    else:
        a -= 1
        print('-1')