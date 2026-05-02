# Program to showcase working of different types of bitwise operators
num1 = 10
num2 = 4 
# Using AND operator
print("num1 & num2 =", num1 & num2)
# Using OR operator
print("\nnum1 | num2 =", num1 | num2)
# Using NOT operator
print("\n~num1 =", ~num1)
# Using XOR operator
print("\nnum1 ^ num2 =", num1 ^ num2)
 
num1 = 10
num2 = 4
 
# Using Right Shift operator on num1
print("\nnum1 >> 1 =", num1 >> 1)
# Using Right Shift operator on num2
print("\nnum2 >> 1 =", num2 >> 1)
 
num1 = 10
num2 = 4
 
# Using Left Shift  operator on num1
print("\nnum1 << 1 =", num1 << 1)
# Using Left Shift operator on num2
print("\nnum2 << 1 =", num2 << 1)

def isEvenOdd(n) :
    if (n ^ 1 == n + 1) :
        return True;
    else :
        return False;
number = int(input("Enter your number : "))
if isEvenOdd(number):
    print(number," is Even")
else:
    print(number," is Odd")

def numberOfBits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1         
    return count 
number = int(input("Enter your number : "))
print("Total bits : ",numberOfBits(number))
