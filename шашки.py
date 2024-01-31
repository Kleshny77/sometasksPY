x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
if y2 > y1:
    if x1 % 2 == y1 % 2:
        if x2 % 2 == y2 % 2:
            print('YES')
        else:
            print('NO')
    else:
        if x2 % 2 != y2 % 2:
            print('YES')
        else:
            print('NO')
else:
    print('NO')