N = int(input('N = '))
dic = {}
dic1 = {}
for i in range(N - 1):
    s = input('s = ').split()
    dic[s[0]] = s[1]
    dic1[s[0]] = 0
for i in dic:
    cnt = 1
    x = dic[i]
    while x in dic:
        x = dic[x]
        cnt += 1
    dic1[i] = cnt
    if x not in dic:
        dic1[x] = 0
sorted_keys = sorted(dic1.keys())
for key in sorted_keys:
    print(key, dic1[key])