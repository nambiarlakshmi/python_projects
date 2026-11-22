def min_coin_rec(coins, n, summ):
    if summ == 0:
        return 1
    if summ < 0:
        return 0
    if n <= 0:
        return 0
    return min_coin_rec(coins, n-1, summ) + min_coin_rec(coins, n, summ-coins[n-1])

coins = [1, 2, 3]
n = len(coins)
print(min_coin_rec(coins, n, 4))