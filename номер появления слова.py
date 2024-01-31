from sys import stdin

s = ''
for line in stdin:
    s += line.rstrip('\n')
dic = {}
s = s.replace(',', ', ').replace(';','; ').replace('.', '. ').split()
a = [0] * len(s)
for i in range(len(s)):
    a[i] += s[:i].count(s[i])
print(*a)