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
cnt = 0
print(array)
for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            cnt += 1
print(cnt)