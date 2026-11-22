def sum_dp(n):
    t = [0] * (n+1)
    t[0] = 0
    for i in range(1, n + 1):
        t[i] = t[i-1] + i
    return t[n]
print(sum_dp(5))