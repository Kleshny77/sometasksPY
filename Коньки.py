str1 = input("Доступные коньки = ").split()
str2 = input("Запрашиваемые коньки = ").split()
cnt = 0
for i in range(len(str2)):
    if str2[i] in str1:
        cnt += 1
        str1.pop(str1.index(str2[i]))
print(cnt)