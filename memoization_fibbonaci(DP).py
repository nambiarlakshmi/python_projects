def fabonacci(n, memo):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fabonacci(n-1, memo) + fabonacci(n - 2, memo)
    return memo[n]
memo = {}
print(fabonacci(6, memo))