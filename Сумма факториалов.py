import sys
n = input('n = ')
if str.isdigit(n):
    n = int(n)
else:
    sys.exit()
def f(x):
    if x == 1:
        return 1
    else:
        return x * f(x - 1)
summ = 0
for i in range(1, n + 1):
    summ += f(i)
print(summ)