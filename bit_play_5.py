# Program to find the number of bits needed to be swapped to make 2 numbers equal
 
def totalFlips(number1, number2):
     
    # Variable to count flips required
    flips = 0
     
    # Get the last bit of both numbers and check of both are same if yes no flip required else flip is required
    while(number1 > 0 or number2 > 0):
        t1 = (number1 & 1)
        t2 = (number2 & 1)
        if(t1 != t2):
            flips += 1
             
        # Right shift both numebrs
        number1>>=1
        number2>>=1
     
    return flips
     
number1 = int(input("Enter First number : "))
number2 = int(input("Enter Second number : "))
 
print("\nNumber of flips needed : ",totalFlips(number1, number2))

# Program to find power set of a set
 
import math;
 
def printPowerSet(set,SetSize):
    
    # Find total elements possible in the power set
    PowerSetSize = (int) (math.pow(2, SetSize));
    outer = 0;
    inner = 0;
    
    for outer in range(0, PowerSetSize):
        for inner in range(0, SetSize):
            # Check if inner bit in the outer is set If set then print inner element from set
            if((outer & (1 << inner)) > 0):
                print(set[inner], end = "")
        print("")
 
size = int(input("Enter array size : "))
 
set = []
for i in range(0,size):
    n = int(input("Enter element : "))
    set.append(n)
 
printPowerSet(set, len(set))