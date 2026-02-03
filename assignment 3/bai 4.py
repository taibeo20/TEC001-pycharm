correct_username = "python"
correct_password = "rules"
attempts = 0

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
        print(f"Wrong information. You have {5 - attempts} attempts to try again later.")

if attempts == 5:
    print("Access denied")