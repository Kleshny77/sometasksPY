import sys

try:
    n = int(input('n = '))
    if n < 3:
        print('ERROR')
        sys.exit()
    arr = list(map(int, input('arr = ').split()))
    arr2 = arr.copy()
    arr3 = []
    arr.sort(reverse=True)
    vasily_place = 0
    for i in range(n):
        if arr[i] % 10 == 5:
            vasily_index = arr2.index(arr[i])
            if vasily_index > 0 and arr2[vasily_index - 1] < arr[i]:
                vasily_place = i + 1
                break

    print(vasily_place)

except ValueError:
    print('ERROR')
    sys.exit()
