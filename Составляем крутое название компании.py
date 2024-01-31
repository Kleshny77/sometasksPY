m = input('s = ').replace('[', ' ').replace(']', ' ')\
        .replace('"', ' ').replace(',', ' ')\
        .split(' ')
s = []
for i in range(len(m)):
    if m[i] != '':
        s.append(m[i])
s1 = set(s)
cnt = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i][0] + s[j][1:] not in s1 and s[j][0] + s[i][1:] not in s1:
            cnt += 2
print(cnt)