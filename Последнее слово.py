import re
text = input("string = ")
pattern = re.compile(r'\b\w+\b')
words = re.findall(pattern, text)
for sentence in re.split(r'[.!?]', text):
    sentence = sentence.strip()
    if sentence:
        last_word = re.findall(pattern, sentence)[-1]
        print(last_word)