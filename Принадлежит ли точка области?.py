import sys

def isPointInArea(x, y):
    return y <= 2 * x + 2 and y <= -x and (x + 1) ** 2 + (y - 1) ** 2 >= 2 ** 2 \
        or y >= 2 * x + 2 and y >= -x and (x + 1) ** 2 + (y - 1) ** 2 <= 2 ** 2

try:
    a = float(input('x = '))
    b = float(input('y = '))
except ValueError:
    sys.exit()

if isPointInArea(a, b):
    print('YES')
else:
    print('NO')