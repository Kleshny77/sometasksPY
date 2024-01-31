import sys

try:
    n = int(input('count = '))
except ValueError:
    sys.exit()

str_array = input('array = ').split()
array = []
for i in range(len(str_array)):
    try:
        q = int(str_array[i])
    except ValueError:
        sys.exit()
    array.append(q)

for i in range(0, len(array), 2):
    print(array[i], end=' ')