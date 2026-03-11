"""Write a Python program first to take a number as an input from the user, then check whether that
 number is even or odd and print the result."""

number = int( input("Enter a number: "))


if (number % 2 == 0):
    print("Even")
elif (number % 2 == 1):
    print("odd")
else:
    print("Error. Enter a whole number.")    
