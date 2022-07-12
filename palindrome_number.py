#get the data from user

Number = input("Enter the number to is palindrome or not :")

if Number == str(Number)[::-1] :
    print("This is palindrome number")
else:
    print("This is not a palindrome number")


choice = input("enter y to continue n to exit ")
if choice == 'y':
        print(Number)

print("thanks you for using")










