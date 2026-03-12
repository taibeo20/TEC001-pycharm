seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter month (1-12): "))

index = (month % 12) // 3
print("Season:", seasons[index])