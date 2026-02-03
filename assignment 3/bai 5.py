text = input("Enter a string: ")
def middle_char(s):
    length = len(s)
    mid = length // 2

    if length % 2 == 0:
        return s[mid - 1: mid + 1]
    else:
        return s[mid]

print("Middle character:", middle_char(text))
