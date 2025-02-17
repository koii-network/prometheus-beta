def count_unique_paths(m: int, n: int) -> int:
    """
    Count the number of unique paths from top-left to bottom-right in an m x n grid.
    
    Only can move either down or right at any point in time.
    
    Args:
        m (int): Number of rows in the grid
        n (int): Number of columns in the grid
    
    Returns:
        int: Number of unique paths to reach bottom-right from top-left
    
    Raises:
        ValueError: If m or n is less than or equal to 0
    """
    # Validate input
    if m <= 0 or n <= 0:
        raise ValueError("Grid dimensions must be positive integers")
    
    # Create a 2D array to store number of paths for each cell
    dp = [[1] * n for _ in range(m)]
    
    # Calculate paths for each cell
    for i in range(1, m):
        for j in range(1, n):
            # Number of paths to current cell is sum of paths from top and left
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # Return total number of unique paths to bottom-right
    return dp[m-1][n-1]