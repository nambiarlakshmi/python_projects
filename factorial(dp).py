def fac_dp(n):
    t = [0] * (n+1)
    t[0] = 1
    for i in range(1, n+1):
        t[i] = t[i-1] * i
    return t[n]
b = int(input("Enter a number: "))
ans = fac_dp(b)
print(ans)

