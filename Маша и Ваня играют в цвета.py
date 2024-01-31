import sys

x = input('x = ')
if x.count('A') + x.count('B') != len(x):
    sys.exit()
flag = False
while x.count('AAA') >= 1 or x.count('BBB') >= 1:
    if x.count('AAA') >= 1:
        x = x.replace('AAA', 'AA', 1)
        flag = True
    if x.count('BBB') >= 1:
        x = x.replace('BBB', 'BB', 1)
        flag = False
print(flag)