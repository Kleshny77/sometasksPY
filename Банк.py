from sys import stdin

data = stdin.readlines()
a = []
dic = {}
for i in range(len(data) - 1):
    data[i] = data[i][:-1]
    a.append(data[i])
if len(data) != 0:
    a.append(data[-1])
for i in range(len(a)):
    a[i] = a[i].split()

for i in a:
    if i[0] in ['DEPOSIT', 'WITHDRAW', 'BALANCE', 'TRANSFER', 'INCOME']:
        if i[0] == 'DEPOSIT':
            if i[1] in dic:
                dic[i[1]] += int(i[-1])
            else:
                dic[i[1]] = int(i[-1])
        if i[0] == 'WITHDRAW':
            if i[1] in dic:
                dic[i[1]] -= int(i[-1])
            else:
                dic[i[1]] = -int(i[-1])
        if i[0] == 'BALANCE':
            if i[1] in dic:
                print(dic[i[1]])
            else:
                print('ERROR')
        if i[0] == 'TRANSFER':
            if i[1] in dic:
                dic[i[1]] -= int(i[-1])
            else:
                dic[i[1]] = -int(i[-1])
            if i[2] in dic:
                dic[i[2]] += int(i[-1])
            else:
                dic[i[2]] = int(i[-1])
        if i[0] == 'INCOME':
            for j in dic:
                if dic[j] > 0:
                    dic[j] = int(dic[j] * (1 + int(i[1]) / 100))
    else:
        print('Invalid Data!')