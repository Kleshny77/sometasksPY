x = input('x = ')
cnt = 0
clon = x
for i in range(len(x)):
    if x[i] == 'h':
        cnt += 1
        if cnt != 1 and cnt != clon.count('h'):
            x = x[:i] + 'H' + x[i + 1:]
print(x)