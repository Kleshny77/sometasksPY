def alf(str1, str2):
    while (str1 != str2):
        print(str1)
        x = ord(str1)
        x += 1
        str1 = chr(x)
alf('abb', 'abc')
