count = 0
for i in range(10):
    word = input('word = ')
    if word[0] == 'S' and word.count('i') >= 1 and len(word) == 6:
        count += 1
print(count)