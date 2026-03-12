numbers = []

while True:
    s = input("Enter number: ")
    if s == "":
        break
    numbers.append(float(s))

numbers.sort(reverse=True)

print("Top 5 greatest numbers:")
print(numbers[:5])