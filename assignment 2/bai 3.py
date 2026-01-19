def check_hemoglobin():
    sex = input("Enter your biological sex (male/female): ").lower().strip()
    try:
        hg_value = float(input("Enter your hemoglobin value (g/l): "))

        if sex == "female":
            if 117 <= hg_value <= 155:
                print("Your hemoglobin value is normal.")
            elif hg_value < 117:
                print("Your hemoglobin value is low.")
            else:
                print("Your hemoglobin value is high.")
        elif sex == "male":
            if 134 <= hg_value <= 167:
                print("Your hemoglobin value is normal.")
            elif hg_value < 134:
                print("Your hemoglobin value is low.")
            else:
                print("Your hemoglobin value is high.")
        else:
            print("Invalid sex input.")
    except ValueError:
        print("Invalid hemoglobin value.")


if __name__ == "__main__":
    check_hemoglobin()