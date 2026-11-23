def edc(str1, str2):
    count = 0
    count += len(str1) - len(str2)
    b = min(len(str1), len(str2))
    for i in range(b):
        if str1[i] != str2[i]:
            count += 1
    return count
str1 = "book"
str2 = "back"
ans = edc(str1, str2)
print("Edit Distance = ", ans)