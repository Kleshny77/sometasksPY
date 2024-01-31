import sys

def f():
    x, y = input('x, y = ').split()
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        sys.exit()
    return x, y

x1, y1 = f()
x2, y2 = f()
x3, y3 = f()
x4, y4 = f()
x5, y5 = f()
x6, y6 = f()
x7, y7 = f()
x8, y8 = f()

a = []
def f(x, y):
    for i in range(1, x + 1):
        if [i, y] not in a:
            a.append([i, y])
        else:
            return False
    for i in range(x + 1, 9):
        if [i, y] not in a:
            a.append([i, y])
        else:
            return False
    for i in range(1, y + 1):
        if [x, i] not in a:
            a.append([x, i])
        else:
            return False
    for i in range(y + 1, 9):
        if [x, i] not in a:
            a.append([x, i])
        else:
            return False
    temp_x, temp_y = x, y
    while temp_x < 8 and temp_y < 8:
        temp_x += 1
        temp_y += 1
        if [temp_x, temp_y] not in a:
            a.append([temp_x, temp_y])
        else:
            return False
    temp_x, temp_y = x, y
    while temp_x > 1 and temp_y > 1:
        temp_x -= 1
        temp_y -= 1
        if [temp_x, temp_y] not in a:
            a.append([temp_x, temp_y])
        else:
            return False
    temp_x, temp_y = x, y
    while temp_x < 8 and temp_y > 1:
        temp_x += 1
        temp_y -= 1
        if [temp_x, temp_y] not in a:
            a.append([temp_x, temp_y])
        else:
            return False
    temp_x, temp_y = x, y
    while temp_x > 1 and temp_y < 8:
        temp_x -= 1
        temp_y += 1
        if [temp_x, temp_y] not in a:
            a.append([temp_x, temp_y])
        else:
            return False
    return True
if f(x1, y1) and f(x2, y2) and f(x3, y3) and f(x4, y4) and \
        f(x5, y5) and f(x6, y6) and f(x7, y7) and f(x8, y8):
    print('YES')
else:
    print('NO')