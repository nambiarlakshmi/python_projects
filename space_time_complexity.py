""" StrongArms"""
# Program to find if a number is Armstrong number
 
# Take input from the user
number = int(input("Input your number: "))
 
# Calculate number of digits
digits = len(str(number))
 
# Initialize result variable
resultNumber = 0
 
# find the sum of the a^digits of each digit
temp = number
while temp > 0:
   digit = temp % 10
   resultNumber += digit ** digits
   temp //= 10
 
# display the result
if number == resultNumber:
   print(number,"is an Armstrong number")
else:
   print(number, "is not an Armstrong number")
   
""" Thats a fact """
# To find factors of user input
 
# Goes from 1 to number and checks if I divide the number. If yes, it is a factor
def print_factors(number):
   print("The factors of",number,"are:")
   for i in range(1, number + 1):
       if number % i == 0:
           print(i)
 
# Taking input from the user
number = int(input("Enter your number to find it's factors: "))
 
# Calling our function
print_factors(number)


""" Roman to Int"""
# Program to convert roman numerals to integers
 
def romanToInt(romanInput):
 
    # All roman units with integer equivalent values
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
 
    #  result
    resultInteger = 0
 
    # Go from 0 to len-1 if integer equivalent is greater than next element then add it else subtract it
 
    for i in range(0, len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger += roman[romanInput[i]]      
    return resultInteger + roman[romanInput[-1]]
 
# Take roman as input from user
roman = input("Input roman numeral : ")
 
# Print the integer
print("Integer equivalent : ",romanToInt(roman))
