def add(n, i = 0):
    if n == 0:
        return i
    m = i + n
    b = add(n-1, m)
    return b
n = int(input("Enter a number:" ))
print(add(n))