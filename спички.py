import sys

l1 = input('l1 = ')
if l1.isdigit():
    l1 = int(l1)
else:
    sys.exit()
r1 = input('r1 = ')
if r1.isdigit():
    r1 = int(r1)
else:
    sys.exit()
l2 = input('l2 = ')
if l2.isdigit():
    l2 = int(l2)
else:
    sys.exit()
r2 = input('r2 = ')
if r2.isdigit():
    r2 = int(r2)
else:
    sys.exit()
l3 = input('l3 = ')
if l3.isdigit():
    l3 = int(l3)
else:
    sys.exit()
r3 = input('r3 = ')
if r3.isdigit():
    r3 = int(r3)
else:
    sys.exit()
while l1 > l2 or l2 > l3 or l1 > l3:
    if l3 < l2:
        l2, l3 = l3, l2
        r2, r3 = r3, r2
    elif l3 == l2:
        if r3 < r2:
            r2, r3 = r3, r2
    if l2 < l1:
        l1, l2 = l2, l1
        r1, r2 = r2, r1
    elif l2 == l1:
        if r2 < r1:
            r2, r3 = r3, r2
if (l2 <= r1 <= r2 >= l3 and r2 <= r3 or l1 <= l3 and r1>= r3):
    print(0)
elif (r1 < l2 and r2 >= l3 and r2 <= r3):
    print(1)
elif (r1 < l2 and r2 < l3 and (r1 - l1 >= l3 - r2)):
    print(1)
elif (r1 >= l2 and r1 <= r2 and r2 < l3):
    print(3)
elif (r1 < l2 and r2 < l3 and (r3 - l3 >= l2 - r1)):
    print(3)
elif (r1 < l2 and r2 < l3 and (r1 - l1 < l3 - r2 or r3 - l3 < l2 - r1)):
    print(-1)
