while True:
    inches = float(input("Enter_inch: "))
    if inches < 0:
        break
    cm = inches * 2.54
    print(f"{inches} inches = {cm} cm")