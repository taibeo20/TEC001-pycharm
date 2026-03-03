import re

def Valid_course(s):
    pattern = r'^[A-Z]{3}[0-9]{3}$'
    return bool(re.match(pattern, s))

code = input("Enter : ")

if Valid_course(code):
    print("True")
else:
    print("False")