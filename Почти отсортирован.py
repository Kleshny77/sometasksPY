import sys

str_array = input('array = ').split()
array = []
for i in range(len(str_array)):
    try:
        q = int(str_array[i])
    except ValueError:
        sys.exit()
    array.append(q)

for i in range(len(array)):
    array2 = array.copy()
    array2.pop(i)
    if array2 == sorted(array2):
        print('Yes')
        break
else:
    print('No')