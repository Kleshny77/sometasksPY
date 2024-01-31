import sys

x = input('x = ')
if x.isdigit() and int(x) > 0:
    x = int(x)
else:
    sys.exit()
result = ''
while x > 0:
        a = (x - 1) % 26
        result = chr(ord('A') + a) + result
        x = (x - 1) // 26
print(result)