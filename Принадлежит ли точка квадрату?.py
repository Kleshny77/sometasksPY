def isPointInSquare(x, y):
    return y <= x + 1 and y <= -x + 1 and y >= -x - 1 and y >= x - 1

a = float(input('x = '))
b = float(input('y = '))
if isPointInSquare(a,b):
    print('YES')
else:
    print('NO')