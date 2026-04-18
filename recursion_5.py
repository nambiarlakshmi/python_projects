"""********** Reverse number ************"""
def reverseNumber(num):
    if(num > 0):
        last = num%10
        if(num//10>0):
            current_number = reverseNumber((int)(num // 10))
            return last*pow(10,len(str(current_number))) + current_number
        return num
n = int(input("Enter your number : "))
print("Reversed : ",reverseNumber(n))

"""********** Reverse string ************"""

def reverseString(s):
    if len(s) == 1:
        return s[0]
    firstchar = s[0]
    return reverseString(s[1:]) + firstchar
s = "153"
print(reverseString(s))



"""********** Power of 4************"""
n = int(input("Enter your number : "))
 
def checkIfPower(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%4==0):
        return checkIfPower(n/4)
    return False
if(checkIfPower(n)):
    print("Power of 4")
else:
    print("Not power of 4")