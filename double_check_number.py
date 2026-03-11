"""Write a Python program to check whether a number entered by the user is greater than 50 or not. 
Also, if it is greater than 50, then check whether it is odd or even."""

number = int(input("Enter a whole number: "))

if (number > 50):
    print("The number is greater than 50.")
    if (number % 2 == 0):
        print("Even")
    else:
        print("Odd")
else:
    print("The number is less than 50. ")
    