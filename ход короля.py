import sys
n = '0123456789'
x1 = input('x1 = ')
for i in x1:
    if i not in n:
        sys.exit()
x1 = int(x1)
y1 = (input('y1 = '))
for i in y1:
    if i not in y1:
        sys.exit()
y1 = int(y1)
x2 = (input('x2 = '))
for i in x2:
    if i not in n:
        sys.exit()
x2 = int(x2)
y2 = (input('y2 = '))
for i in y2:
    if i not in n:
        sys.exit()
y2 = int(y2)
if abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
    print('YES')
else:
    print('NO')