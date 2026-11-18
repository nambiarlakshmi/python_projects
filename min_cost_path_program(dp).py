def min_cost(grid, col, row):
    r = len(grid)
    c = len(grid[0])
    dp = [[0 for i in range(c)] for j in range(r)]
    dp[0][0] = grid[0][0]

    for i in range(1, row + 1):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, col + 1):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            best_prev = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
            dp[i][j] = best_prev + grid[i][j]
    return dp[row][col]

cost = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]

r = min_cost(cost, 2, 2)
print(r)