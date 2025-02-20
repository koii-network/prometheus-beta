from typing import List

def find_shortest_path(grid: List[List[int]]) -> int:
    """
    Find the shortest path from top-left to bottom-right with movement constraints.
    
    Args:
        grid (List[List[int]]): A square grid of 0s and 1s
    
    Returns:
        int: Length of the shortest path, or -1 if no path exists
    """
    if not grid or not grid[0]:
        return -1
    
    n = len(grid)
    
    # Dynamic programming to track minimum path lengths
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = 1  # Starting point
    
    # Fill first row
    for j in range(1, n):
        if grid[0][j] == 0:
            dp[0][j] = dp[0][j-1] + 1
        else:
            break
    
    # Fill first column
    for i in range(1, n):
        if grid[i][0] == 0:
            dp[i][0] = dp[i-1][0] + 1
        else:
            break
    
    # Fill rest of the DP table
    for i in range(1, n):
        for j in range(1, n):
            # Movement constraints
            if grid[i][j] == 0:
                # Can move right if previous cell is empty
                if grid[i][j-1] == 0:
                    dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1)
                # Otherwise, must move down
                else:
                    dp[i][j] = dp[i-1][j] + 1
    
    # Return path length or -1 if no path exists
    return dp[n-1][n-1] if dp[n-1][n-1] != float('inf') else -1