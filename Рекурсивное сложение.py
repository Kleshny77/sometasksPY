import sys

def Sum(a, b):
    if b == 0:
        return a
    elif b > 0:
        return Sum(a + 1, b - 1)

x, y = input('x, y = ').split()
try:
    x = int(x)
    y = int(y)
except ValueError:
    sys.exit()
except EOFError:
    sys.exit()
print(Sum(x, y))