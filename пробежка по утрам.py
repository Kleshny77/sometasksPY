import sys

x = input('x = ')
if x.isdigit() and int(x) >= 0:
    x = int(x)
else:
    sys.exit()
y = input('y = ')
if y.isdigit() and int(y) >= 0:
    y = int(y)
else:
    sys.exit()
count = 1
while x < y:
    x *= 1.1
    count += 1
print(count)