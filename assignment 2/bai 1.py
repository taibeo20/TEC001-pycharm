def check_zander():
    try:
        length = float(input("Enter the length of the zander in centimeters: "))
        size_limit = 42

        if length >= size_limit:
            print("The zander meets the size limit.")
        else:
            diff = size_limit - length
            print("Please release the fish back into the lake.")
            print(f"The fish was {diff:.1f} cm below the size limit.")
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    check_zander()