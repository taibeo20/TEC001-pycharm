def filter_even_numbers(numbers):
    even_list = []
    for n in numbers:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

def main():
   original_list = [1,2,3,4,5,6,7,8,9]
   cut_down_list = filter_even_numbers(original_list)
   print(original_list)
   print(cut_down_list)

if __name__ == "__main__":
    main()