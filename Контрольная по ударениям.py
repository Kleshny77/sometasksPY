N = int(input('N = '))
s = set()
s1 = set()
for i in range(N):
    x = input('s = ')
    s.add(x)
    s1.add(x.lower())
a = input('a = ').split()
cnt = 0
for i in a:
    if i.lower() in s1:
        if i not in s:
            cnt += 1
    else:
        tmp = 0
        for j in i:
            if j.isupper():
                tmp += 1
                if tmp == 2:
                    cnt += 1
                    break
        if tmp != 1:
            cnt += 1
print(cnt)