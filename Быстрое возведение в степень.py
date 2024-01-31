import sys

a, n = input('x, y = ').split()
try:
    a = float(a)
    n = float(n)
except ValueError:
    sys.exit()

def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(a, n // 2) * pow(a, n // 2)
    else:
        return a * pow(a, n - 1)
print(pow(a, n))