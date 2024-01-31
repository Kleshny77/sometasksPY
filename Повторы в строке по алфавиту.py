import sys

x = input('x = ')
if not x.isalpha():
    sys.exit()

while True:
    length = len(x)
    for i in range(len(x) - 1, 0, -1):
        if x.count(x[i]) > 1:
            if x.rstrip(x[i]) <= x.lstrip(x[i]):
                x = x.rstrip(x[i])
            else:
                x = x.lstrip(x[i])
    if len(x) == length:
        break
print(x)