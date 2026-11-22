def cc(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    # Solve subproblem for each amount from 1 to targer
    for i in range(1, amount + 1):
        # Try using each coin denomination
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == float("inf"):
        return -1
    else:
        return dp[amount]
coin = [1,2,5]
amount = 11
result = cc(coin, amount)
print(f"The minimum number of coins needed: {result}")