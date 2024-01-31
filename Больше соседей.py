import sys
def correct(x):
    try:
        int(x)
    except ValueError:
        sys.exit()
    return True
n = input('n = ')
if correct(n):
    n = int(n)
cnt = 0
array_str = input('array = ').split()
array = []
for i in range(len(array_str)):
    if correct(array_str[i]):
        array.append(int(array_str[i]))
for h in range(1, len(array) - 1):
    if array[h - 1] < array[h] > array[h + 1]:
        cnt += 1
print(cnt)