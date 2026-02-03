smallest = None
largest = None

while True:
    user_input = input("Enter a number : ")

    if user_input == "":
        break

    try:
        num = float(user_input)

        if smallest is None or num < smallest:
            smallest = num

        if largest is None or num > largest:
            largest = num

    except ValueError:
        print("Please enter a valid number.")

if smallest is not None:
    print("Smallest number:", smallest)
    print("Largest number:", largest)
else:
    print("No numbers were entered.")
