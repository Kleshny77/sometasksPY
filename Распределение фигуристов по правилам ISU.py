import sys

try:
    n = int(input('number = '))
except ValueError:
    sys.exit()
a = []
while n > 0:
    if n - 6 >= 0:
        n -= 6
        a.append(6)
    else:
        a.append(n)
        break

for i in range(len(a) - 1):
    if a[i] - a[i + 1] > 1:
        min(a[i], a[i + 1]) += 1
        max(a[i], a[i + 1]) -= 1
a.reverse()
print(*a, sep='+')