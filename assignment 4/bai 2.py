a = int(input ("Enter a number: "))
if (a == 2):
    print("prime")
elif (a < 2):
    print('not prime')
else:
    for i in range(2, a+1):
        if a % i == 0:
            print ('not prime')
            break
        elif i == a:
            print ('prime')