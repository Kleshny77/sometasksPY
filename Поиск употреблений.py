import re
def find_duplicate_words(text):
    pattern = r'\b(\w+)\b\s+\1\b'
    duplicates = re.findall(pattern, text)
    return duplicates
input_text = input("str = ")
result = find_duplicate_words(input_text)
for i in result:
    print(i)