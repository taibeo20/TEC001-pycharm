text = input("Enter a phrase: ")
def acronym(phrase):
    words = phrase.split()
    result = ""

    for word in words:
        result += word[0].upper()

    return result
print("Acronym:", acronym(text))
