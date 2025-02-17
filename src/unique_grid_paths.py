def count_unique_paths(m: int, n: int) -> int:
    """
    Count the number of unique paths from top-left to bottom-right 
    in an m x n grid, moving only right or down.
    
    Args:
        m (int): Number of rows in the grid
        n (int): Number of columns in the grid
    
    Returns:
        int: Number of unique paths
    
    Raises:
        ValueError: If m or n is less than 1
    """
    # Validate input
    if m < 1 or n < 1:
        raise ValueError("Grid dimensions must be positive integers")
    
    # Create a 2D dynamic programming table to store path counts
    dp = [[1] * n for _ in range(m)]
    
    # Fill the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # Return the total number of unique paths
    return dp[m-1][n-1]