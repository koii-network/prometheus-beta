def rod_cutting(prices, n):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
        prices (list): A list of prices for rod lengths from 1 to len(prices)
        n (int): The length of the rod to cut
    
    Returns:
        int: The maximum obtainable value by cutting the rod
    
    Raises:
        ValueError: If input is invalid
    """
    # Input validation
    if not isinstance(prices, list):
        raise ValueError("Prices must be a list")
    if not isinstance(n, int) or n < 0:
        raise ValueError("Rod length must be a non-negative integer")
    
    # Extend prices list if needed, using 0 for non-specified lengths
    prices = prices + [0] * (n - len(prices) + 1)
    
    # Dynamic programming table to store max values
    dp = [0] * (n + 1)
    
    # Compute maximum value for each rod length
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            max_val = max(max_val, prices[j] + dp[i - j])
        dp[i] = max_val
    
    return dp[n]