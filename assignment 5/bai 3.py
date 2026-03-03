import re

def sum_numbers_in_text(text):
    numbers = re.findall(r'\d+', text)
    total = 0

    for num in numbers:
        total += int(num)

    return total


text = input("Enter: ")
result = sum_numbers_in_text(text)
print("sum_numbers:", result)