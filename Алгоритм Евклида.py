import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

x = input('a = ')
y = input('b = ')
try:
    x = int(x)
    y = int(y)
except ValueError:
    sys.exit()

print(gcd(x, y))