def fac(n, i = 1):
    if n == 1:
        return i
    m = i * n
    b = fac(n-1, m)
    return b
print(fac(5))


