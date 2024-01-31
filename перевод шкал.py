import re
def find_word_time(text):
    pattern = r'\bврем(ени|я|ями|ях|ям?|енем)\b'
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    return matches
input_text = input("str = ")
result = find_word_time(input_text)
print(result)