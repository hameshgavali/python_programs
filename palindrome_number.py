condi = True

while condi:
    Number = input("Enter the data  to check is  palindrome or not :")

    if Number == Number[::-1]:
        print("This is palindrome ")
    else:
        print("This is not a palindrome ")

    choice = input("Do you want to continue [y/n] ")
    if choice == 'n':
        print("thanks you for using")
        condi = False
