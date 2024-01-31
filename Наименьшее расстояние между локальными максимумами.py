import sys

x = input('x = ')
if x.isdigit():
    x = int(x)
else:
    sys.exit()
count = 1
max1 = 0
max2 = 0
count_max1 = 0
count_max2 = 0
while x != 0:
    if x >= max2:
        max2, max1 = x, max2
        count_max2, count_max1 = count, count_max2
    count += 1
    x = input('x = ')
    if x.isdigit():
        x = int(x)
    else:
        sys.exit()
print(count_max2 - count_max1)