def keep_even(numbers):
    even = []
    for n in numbers:
        if n % 2 == 0:
            even.append(n)
    return even

n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

even_numbers = keep_even(numbers)

print(numbers)
print(even_numbers)