import math


def calculate_unit_price(diameter_cm, price_usd):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * (radius_m ** 2)

    if area_m2 == 0:
        return 0
    return price_usd / area_m2


def compare_pizzas():
    try:
        d1 = float(input("Enter diameter of pizza 1 (cm): "))
        p1 = float(input("Enter price of pizza 1 (USD): "))
        price_per_m2_1 = calculate_unit_price(d1, p1)
        print(f"Unit price of pizza 1: {price_per_m2_1:.2f} USD/m2")

        d2 = float(input("Enter diameter of pizza 2 (cm): "))
        p2 = float(input("Enter price of pizza 2 (USD): "))
        price_per_m2_2 = calculate_unit_price(d2, p2)
        print(f"Unit price of pizza 2: {price_per_m2_2:.2f} USD/m2")

        if price_per_m2_1 < price_per_m2_2:
            print("Pizza 1 provides better value for money.")
        elif price_per_m2_2 < price_per_m2_1:
            print("Pizza 2 provides better value for money.")
        else:
            print("Both pizzas have the same value.")

    except ValueError:
        print("Invalid input numbers.")


if __name__ == "__main__":
    compare_pizzas()