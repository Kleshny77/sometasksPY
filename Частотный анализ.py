from sys import stdin

s = ''
for line in stdin:
    s += line.replace('\n', ' ')
s = s.split()
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
for i in dic:
    print(i[0])
