import sys

def sort_arr(arr, k):
    l = len(arr)
    for q in range(l):
        column = [arr[i][q] for i in range(l)]
        column.sort(key=lambda x: (abs(x - k), x))
        for w in range(l):
            arr[w][q] = column[w]
    return arr

try:
    n, t = map(int, input().split())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    sorted_matrix = sort_arr(matrix, t)
    for i in sorted_matrix:
        for j in i:
            print(j, end=' ')
        print('')
except ValueError:
    print("ERROR")
    sys.exit()