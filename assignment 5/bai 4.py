import re

def hide_phone_numbers(text):
    pattern = r'(\+84\d+|\d{10})'
    return re.sub(pattern, '[REDACTED]', text)


text = input("Enter: ")
result = hide_phone_numbers(text)
print(result)