def rod_cutting(prices, n):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
    prices (list): List of prices for rod lengths from 1 to len(prices)
    n (int): Length of the rod to cut
    
    Returns:
    int: Maximum obtainable value by cutting the rod
    """
    # Create a dynamic programming table to store maximum values
    # dp[i] represents the maximum value obtainable for a rod of length i
    dp = [0] * (n + 1)
    
    # Build the solution bottom-up
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, min(i, len(prices)) + 1):
            # Try cutting the rod into pieces of length j
            max_val = max(max_val, prices[j-1] + dp[i-j])
        dp[i] = max_val
    
    return dp[n]