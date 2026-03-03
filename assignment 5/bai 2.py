import re

def is_valid_hex_color(s):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(pattern, s))


color = input("Enter: ")

if is_valid_hex_color(color):
    print("True")
else:
    print("False")