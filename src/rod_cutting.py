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
        max_val = float('-inf')
        for j in range(1, i + 1):
            # Either don't cut or cut into pieces
            max_val = max(max_val, prices[j-1] + dp[i-j])
        dp[i] = max_val
    
    return dp[length]