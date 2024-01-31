import sys
import math
try:
    x1 = int(input('x1 = '))
    x2 = int(input('x2 = '))
    x3 = int(input('x3 = '))
except ValueError:
    print("ERROR")
    sys.exit()

cnt = math.ceil(x1 / 2) + math.ceil(x2 / 2) + math.ceil(x3 / 2)
print(cnt)