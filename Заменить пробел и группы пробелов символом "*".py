x = input('x = ')
while x.count('  ') != 0:
    x = x.replace('  ', ' ')
x = x.replace(' ', '*')
print(x)