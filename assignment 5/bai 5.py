import random


def approximate_pi(N):
    inside_circle = 0

    for i in range(N):  # dùng i thay vì _
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / N
    return pi_estimate

N = int(input("Enter total number of random points: "))

result = approximate_pi(N)

print("The approximate value of pi is:", result)