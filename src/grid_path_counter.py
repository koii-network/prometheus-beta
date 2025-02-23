def count_unique_paths(m: int, n: int) -> int:
    """
    Count the number of unique paths from top-left to bottom-right corner in an m x n grid.
    
    A robot can only move either down or right at any point in time.
    
    Args:
        m (int): Number of rows in the grid (must be positive)
        n (int): Number of columns in the grid (must be positive)
    
    Returns:
        int: Total number of unique paths from top-left to bottom-right
    
    Raises:
        ValueError: If m or n is less than or equal to 0
    
    Example:
        >>> count_unique_paths(3, 7)
        28
        >>> count_unique_paths(3, 2)
        3
    """
    # Validate input
    if m <= 0 or n <= 0:
        raise ValueError("Grid dimensions must be positive integers")
    
    # Create a 2D dynamic programming table to store path counts
    dp = [[1] * n for _ in range(m)]
    
    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            # Number of paths to current cell is sum of paths from above and left
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # Return total number of unique paths
    return dp[m-1][n-1]