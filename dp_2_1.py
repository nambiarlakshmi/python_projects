def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range (capacity + 1)] for _ in range( n +1)]
    for i in range(1, n+1):
        for j in range(1, capacity +1):
            if weights[i - 1] <= j:
                dp [i][j] = max(dp[i -1][j],values[i -1] + dp[i - 1] [j - weights[i -1]] )
            else:
                dp[i][j] = dp[i -1] [j]
    max_value = dp[n][capacity]
    items_in_knapsack = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i -1][j]:
            items_in_knapsack.append(i - 1)
            j -= weights[i -1]
    return max_value, items_in_knapsack[::-1]
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
max_value, items_in_knapsack = knapsack_01(weights, values, capacity)
print("Maximum value in knapsack:", max_value)
print("Items inclueded in the knapsack:", items_in_knapsack)


def subset_sum(set_elements, target_sum):
    n = len(set_elements)
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n +1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, target_sum +1):
            if set_elements[i - 1] <= j:
                dp[i][j] = dp [i-1][j] or dp[i -1][j-set_elements[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target_sum]

set_elements = [3, 34, 4, 12, 5, 2]
target_sum = 9
if subset_sum(set_elements, target_sum):
    print("There is a subset with the target sum.")
else:
    print("There is no subset with the target sum.")