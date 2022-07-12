condi = True

while condi:
    Data = input("Enter the data  to check is  palindrome or not :")

    if Data == Data[::-1]:
        print("This is palindrome ")
    else:
        print("This is not a palindrome ")

    choice = input("Do you want to continue [y/n] ")
    if choice == 'n':
        print("thanks you for using")
        condi = False
