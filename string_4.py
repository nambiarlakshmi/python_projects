""" ******BARCODE ****** """
"""Write a program to determine the price of an item using the given BARCODE. Barcode consists of letters (uppercase and lowercase) of the alphabet, numeric characters (0 to 9) and special symbols. The shopkeeper wants to find every character's ASCII value on the Barcode. He has to note down only the maximum digit, if it is a 2-digit or 3-digit code for each character. The product's final price will be the sum of all numbers obtained from the ASCII codes of each character on the Barcode."""

# Count how many times each letter comes in a word
def frequency(word):
    word = word.replace(" ", "").lower()  # remove spaces + make all letters small
    counts = {}

    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    return counts

# Check if two words are anagrams (same letters, same count)
def checkAnagrams(word1, word2):
    if frequency(word1) == frequency(word2):
        return True
    else:
        return False

# Driver code
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

print(checkAnagrams(word1, word2))

"""lexicographicallyNext****"""
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