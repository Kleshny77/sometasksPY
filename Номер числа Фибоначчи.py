import sys

try:
    n = int(input('number = '))
except ValueError:
    sys.exit()

def f(x):
    if x <= 0:
        return -1
    elif x == 1:
        return 1
    fib1 = 1
    fib2 = 1
    flag = True
    for i in range(3, 10000):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        if fib3 == x:
            flag = False
            return i
    if flag:
        return -1
print(f(n))