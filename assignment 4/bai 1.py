array = []
a = input('Enter: ')
while (a.isdigit()):
    array.append(int(a))
    a = input('Enter: ')

array.sort(reverse = True)
print (array[:5])