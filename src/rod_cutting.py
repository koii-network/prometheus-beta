def rod_cutting(prices, length):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
        prices (list): List of prices for each rod length (1-indexed).
        length (int): Total length of the rod to cut.
    
    Returns:
        int: Maximum obtainable value by cutting the rod.
    
    Raises:
        ValueError: If input is invalid.
    """
    # Validate inputs
    if not prices or length <= 0:
        return 0
    
    if len(prices) <= length:
        # Pad prices list if necessary
        prices = prices + [0] * (length - len(prices) + 1)
    
    # Initialize DP table
    dp = [0] * (length + 1)
    
    # Build solution bottom-up
    for i in range(1, length + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            max_val = max(max_val, prices[j] + dp[i - j])
        dp[i] = max_val
    
    return dp[length]