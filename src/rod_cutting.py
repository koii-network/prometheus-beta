def rod_cutting(prices, length):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
    prices (list): List of prices for rod lengths (0-indexed)
    length (int): Total length of the rod
    
    Returns:
    int: Maximum obtainable value by cutting the rod
    """
    # Validate inputs
    if not prices or length <= 0:
        return 0
    
    # Initialize dynamic programming table
    # dp[i] represents the maximum value for a rod of length i
    dp = [0] * (length + 1)
    
    # Build solution bottom-up
    for i in range(1, length + 1):
        max_val = float('-inf')
        for j in range(1, min(i, len(prices)) + 1):
            max_val = max(max_val, prices[j-1] + dp[i-j])
        dp[i] = max_val
    
    return dp[length]