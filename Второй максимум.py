x = int(input('x = '))
a = []
while x != 0:
    a.append(x)
    x = int(input('x = '))
a[a.index(max(a))] = -1
print(max(a))
