""" Time Complexity O(√n) """

from math import sqrt  # O(1)
number = int(input("Enter your number : ")) # O(1)
print("\n") # O(1)
if number > 1: # O(1)
    for i in range(2, int(sqrt(number))+1):  #O(√n) bcoz loop runs from 2 to √n
        if (number % i) == 0:   # O(1)
            print(number, "is not a prime number")  # O(1)
            break  # O(1)
    else:  # O(1)
        print(number, "is a prime number")  # O(1)
else:  # O(1)
    print(number, "is not a prime number")  # O(1)

""" Time Complexity O(nloglogn)"""
def SieveOfEratosthenes(num): 
    prime = [True for i in range(num+1)] #O(n) 
    p = 2  # O(1)
    while (p * p <= num): # O(√n) 
        if (prime[p] == True): # O(1)
            for i in range(p * p, num+1, p): #O( n/p)
                prime[i] = False
        p += 1 # O(1)

    for p in range(2, num+1): # O(n)
        if prime[p]: # O(1)
            print(p) # O(1)

num = int(input("Enter a number")) # O(1)
print("Following are the prime numbers smaller") # O(1)
print("than or equal to", num) # O(1)
SieveOfEratosthenes(num)# O(1)

#  O(n)+ #O( n/p) +O(√n)  = O(nloglogn)​

""" Total Complexity O(n^2) """
a = 3000 # O(1)
for num in range(1,a+1): # O(n)
    c=0 # O(1)
    rev = 0 # O(1)
    temp = num # O(1)
    for i in range (1,temp+1): # O(n)
        if temp%i==0: # O(1)
            c+=1 # O(1) 
    if c==2: # O(1)
        while temp>0: # O(n)
            rev = rev*10+(temp%10) # O(1)
            temp //=10 # O(1)
        if rev == num:# O(1)
            print(num) # O(1)