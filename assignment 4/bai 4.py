def sum(numbers: list):
    total = 0
    for n in numbers:
        total += n
    return total

if __name__ == "__main__":
    my_list = [1,3,5,7,9]
    res = sum(my_list)
    print(f"Sum of list = {res}")