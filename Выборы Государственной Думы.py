import sys
from sys import stdin

array_line = []
for line in stdin:
    array_line.append(line.rstrip('\n'))

dic_golosa = {}
for i in range(len(array_line)):
    array_line[i] = array_line[i].split()
    if len(array_line[i]) > 2:
        name = ''
        for j in range(len(array_line[i]) - 1):
            name += array_line[i][j] + ' '
        try:
            array_line[i] = [name[:-1], int(array_line[i][-1])]
        except ValueError:
            print('ERROR!')
            sys.exit()

for i in array_line:
    dic_golosa[i[0]] = int(i[1])

summ_golosov = 0
for i in dic_golosa:
    summ_golosov += int(dic_golosa[i])

val_perv_izbr_chastn = summ_golosov / 450
dic_mesta_in_parl = {}
summ_mest = 0

for i in dic_golosa:
    dic_mesta_in_parl[i] = dic_golosa[i] // val_perv_izbr_chastn
    summ_mest += dic_mesta_in_parl[i]

if summ_mest < 450:
    ost_mest = 450 - summ_mest
    for i in sorted(dic_mesta_in_parl.keys(), reverse=True):
        dic_mesta_in_parl[i] += 1
        ost_mest -= 1
        if ost_mest == 0:
            break

for i in dic_mesta_in_parl:
    print(i, int(dic_mesta_in_parl[i]))