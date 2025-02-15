def count_unique_paths(m: int, n: int) -> int:
    """
    Calculate the number of unique paths from top-left to bottom-right 
    in an m x n grid, moving only right or down.
    
    Args:
        m (int): Number of rows in the grid
        n (int): Number of columns in the grid
    
    Returns:
        int: Total number of unique paths
    
    Raises:
        ValueError: If m or n is less than 1
    """
    # Input validation
    if m < 1 or n < 1:
        raise ValueError("Grid dimensions must be at least 1x1")
    
    # Create a 2D grid to store path counts
    dp = [[1] * n for _ in range(m)]
    
    # Calculate unique paths using dynamic programming
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]