Number = int(input("Enter the number"))

if Number > 1:
    for i in range(2, Number):
        if Number % i == 0:
            print(f"{Number} is  not prime number ")
            break
    else:
        print(f"{Number} is a prime prime")
else:
    print("not prime")








