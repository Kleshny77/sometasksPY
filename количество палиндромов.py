import sys

k = input('k = ')
if k.isdigit() and 1 <= int(k) <= 100000:
    k = int(k)
else:
    sys.exit()
count = 0
for i in range(1, k + 1):
    x = ''
    n = i
    while i != 0:
        x += str(i % 10)
        i //= 10
    if int(x) == n:
        count += 1
print(count)
