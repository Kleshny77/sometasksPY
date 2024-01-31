import sys
from sys import stdin

data = stdin.readlines()
school = [0] * 99

for line in data:
    try:
        parts = line.split()
        if len(parts) != 4 or not parts[-1].isdigit() or not parts[-2].isdigit():
            raise ValueError
        else:
            school[int(parts[-2])] += 1
    except ValueError:
        print('ERROR!')
        sys.exit()

max_count = max(school)
max_school_index = school.index(max_count)
print(max_count, max_school_index)
