"""****** Countthe frequency ******"""
def frequency(s):
    s = s.lower()  
    d = {}
    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return d
inp = input("Enter String: ")
print(frequency(inp))

"""****** Check anagram ******"""
def frequency(word):
    word = word.replace(" ", "").lower()  
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

def checkAnagrams(word1, word2):
    if frequency(word1) == frequency(word2):
        return True
    else:
        return False
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
print(checkAnagrams(word1, word2))

"""******* Count Words******"""
def countWords(s):
    count = 0
    s = s.strip()
    for i in range(len(s)):
        if s[i] == " ":
            count += 1
    return count + 1 
inp = input("Enter String: ")
print("Number of words: ", countWords(inp))
