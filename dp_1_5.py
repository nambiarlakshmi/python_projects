def coin_change(coins,amount):
    dp = [float('inf')] * (amount +1)
    dp[0] = 0
    for i in range (1,amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]

coin = [1, 2, 5]
amount = 11
result = coin_change(coin, amount)
print(f"The minimum number of coins needed: {result}")

def count(coins, n, sum):
    if (sum == 0):
            return 1
    if (sum < 0):
         return 0
    if(n <= 0):
            return 0
    return count(coins, n - 1, sum) + count(coins, n, sum - coins [n-1])
coins = [1, 2, 4]
n = len(coins)
print(count(coins, n, 4))