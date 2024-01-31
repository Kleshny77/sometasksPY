import sys

def f():
    x = input('x = ')
    try:
        x = int(x)
    except ValueError:
        sys.exit()
    if x != 0:
        f()
    print(x)

f()