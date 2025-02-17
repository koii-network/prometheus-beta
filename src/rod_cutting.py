def rod_cutting(prices, n):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
        prices (list): List of prices for rod lengths from 1 to len(prices)
        n (int): Length of the rod to cut
    
    Returns:
        int: Maximum obtainable value by cutting the rod
    """
    # Handle edge cases
    if n <= 0:
        return 0
    if n > len(prices):
        raise ValueError("Rod length exceeds available price list")
    
    # Initialize dynamic programming table
    dp = [0] * (n + 1)
    
    # Compute maximum value for each rod length
    for length in range(1, n + 1):
        max_val = float('-inf')
        for cut in range(1, length + 1):
            # Check if the current cut length is valid
            if cut <= len(prices):
                max_val = max(max_val, prices[cut - 1] + dp[length - cut])
        dp[length] = max_val
    
    return dp[n]