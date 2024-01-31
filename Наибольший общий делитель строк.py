import sys

str1 = input('str1 = ')
if not str1.isalpha():
    sys.exit()
str2 = input('str2 = ')
if not str2.isalpha():
    sys.exit()
if str1 == str2:
    print(str1)
elif str1.count(str2) >= 1:
    print(str1.replace(str2, '', 1))
elif str2.count(str1) >= 1:
    print(str2.replace(str1, '', 1))
else:
    print(0)