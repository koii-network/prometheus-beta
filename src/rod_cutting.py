def rod_cutting(prices, length):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
        prices (list): List of prices for rod lengths (0-indexed).
                       prices[i] is the price for a rod of length i+1.
        length (int): Total length of the rod to be cut.
    
    Returns:
        int: Maximum obtainable value by cutting the rod.
    
    Raises:
        ValueError: If input is invalid (negative prices or length).
    """
    # Input validation
    if not prices or length < 0:
        return 0
    
    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative")
    
    # Extend prices list if needed
    if len(prices) < length:
        prices = prices + [0] * (length - len(prices))
    
    # Initialize DP table
    dp = [0] * (length + 1)
    
    # Build solution bottom-up
    for i in range(1, length + 1):
        for j in range(1, i + 1):
            # Choose the maximum between current max and current combination
            # Correct access of prices by j-1 to handle 0-indexing
            dp[i] = max(dp[i], prices[j-1] + dp[i-j])
    
    return dp[length]