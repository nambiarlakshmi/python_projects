""" ********** uppercase to lower and lower to uppercase*******"""

def changeTheCase(s):
    result = ""
    for i in s:
        if i.islower():
            result = result + i.upper()
        if i.isupper():
            result = result + i.lower()
    return result

inp = input("Enter String: ")
print("String after change lower case to upper and vice versa-")
print(changeTheCase(inp))


"""******palindrome*******"""
def reverse(s):
    return s[::-1]
def checkPalindrome(s):
    s = s.lower()
    rev_string = reverse(s)
    if s == rev_string:
        return True
    else:
        return False
inp = input("Enter String: ")
print(checkPalindrome(inp))


""" ******** remove vowels*******"""
def removeVowels(s):
    result = ""
    li = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        if s[i] in li:
            result = result + " "
        else:
            result = result + s[i]
    return result
inp = input("Enter String: ")
print("Result:", removeVowels(inp))