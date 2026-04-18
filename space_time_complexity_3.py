"""Total Time Complexity : O(n)"""
number = int(input("Input your number: "))
digits = len(str(number)) 
resultNumber = 0
temp = number
while temp > 0: #O(n)
   digit = temp % 10
   resultNumber += digit ** digits
   temp //= 10
if number == resultNumber:
   print(number,"is an Armstrong number")
else:
   print(number, "is not an Armstrong number")
   
""" Total Time Complexity O(n) """
def print_factors(number): # O(1)
   print("The factors of",number,"are:") # O(1)
   for i in range(1, number + 1): # O(n) / f(n) = n+100 
       if number % i == 0: # O(1)
           print(i) # O(1)
number = int(input("Enter your number to find it's factors: ")) # O(1)
print_factors(number) # O(1)

"""Time complexity O(n²)  """
def ONSquareTime(n): # O(1)
  iteration=0 # O(1)
  for i in range(0,n): # O(n)
    for j in range(0,n):# O(n)
      print("*", end =" ") # O(1)
      iteration+=1 # O(1)
    print("") # O(1)
  print("\nWhen n is ",n," Iterations = ",iteration,"\n") # O(1)
 
ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)
 
print("\nWith every 'n' the time taken equals n^2")
print("O(n^2)")
