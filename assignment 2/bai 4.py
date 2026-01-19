def check_leap_year():
    try:
        year = int(input("Enter a year: "))

        # Năm nhuận chia hết cho 4.
        # Nếu chia hết cho 100 thì cũng phải chia hết cho 400 mới là nhuận.
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    check_leap_year()