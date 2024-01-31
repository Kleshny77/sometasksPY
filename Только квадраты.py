import sys

s = ''
while True:
    try:
        x = int(input('x = '))
    except ValueError:
        sys.exit()
    if x == 0:
        break
    if x ** 0.5 == int(x ** 0.5):
        s += str(x) + ' '
s = s[:-1]
if s == '':
    print(0)
else:
    print(s[::-1])