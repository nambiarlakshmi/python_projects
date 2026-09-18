def naive_search(text, pattern):
    positions = []

    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            positions.append(i)

    return positions


def kmp_search(text, pattern):
    positions = []

    lps = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == len(pattern):
            positions.append(i - j + 1)
            j = lps[j - 1]

    return positions


text = "ababababca"
pattern = "abab"

print("Naive Search:", naive_search(text, pattern))
print("KMP Search:", kmp_search(text, pattern))