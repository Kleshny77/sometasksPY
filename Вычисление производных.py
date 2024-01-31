import sys

str_array = input('Функция = ').split()
array = []
for i in range(len(str_array)):
    try:
        q = int(str_array[i])
    except ValueError:
        sys.exit()
    array.append(q)

try:
    n = int(input('Порядок производной = '))
except ValueError:
    sys.exit()

if n >= 1:
    x = len(array)
    while n != 0:
        for i in range(len(array)):
            array[i] *= x - i - 1
        n -= 1
        x -= 1
while True:
    if array[-1] == 0:
        array.pop(-1)
    else:
        break

print(*array)
