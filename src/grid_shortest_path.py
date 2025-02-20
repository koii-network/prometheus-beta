def find_shortest_path(grid):
    """
    Find the shortest path from top-left to bottom-right with constrained movement.
    
    Args:
    grid (List[List[int]]): 2D grid of 0s and 1s where 0 is empty and 1 is blocked
    
    Returns:
    int: Length of the shortest path, or -1 if no path exists
    """
    if not grid or not grid[0]:
        return -1
    
    n = len(grid)
    
    # Dynamic programming to track path lengths
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = 1  # Starting point
    
    # Fill the first row
    for j in range(1, n):
        # Can only move right if the previous cell is empty and current cell is empty
        if grid[0][j] == 0 and grid[0][j-1] == 0:
            dp[0][j] = dp[0][j-1] + 1
        else:
            break
    
    # Fill the first column
    for i in range(1, n):
        # Can only move down 
        if grid[i][0] == 0:
            dp[i][0] = dp[i-1][0] + 1
        else:
            break
    
    # Fill the rest of the dp table
    for i in range(1, n):
        for j in range(1, n):
            # If current cell is blocked, skip
            if grid[i][j] == 1:
                continue
            
            # Check moving right (if previous cell is empty)
            if j > 0 and grid[i][j-1] == 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
            
            # Check moving down
            if grid[i-1][j] == 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
    
    # Return path length to bottom-right, or -1 if unreachable
    return dp[n-1][n-1] if dp[n-1][n-1] != float('inf') else -1