"""Write a Python program to take a number as input from the user and check whether it is a prime number
 or not"""

x = int(input("Enter a number: "))
if x < 1:
    print("Not Prime")
else:
    i = 2
    is_prime = True
while i <= x//2:
    if x % i == 0:
        is_prime = False
        break
    i += 1
    if is_prime:
        print("It is Prime")
    else:
        print("Not prime")