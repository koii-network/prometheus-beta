def rod_cutting(prices, length):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
    prices (list): A list of prices for rod lengths from 1 to len(prices)
    length (int): The total length of the rod to be cut
    
    Returns:
    int: The maximum obtainable value by cutting the rod
    """
    # Validate input
    if not prices or length <= 0:
        return 0
    
    # Extend prices list if needed to match rod length
    if len(prices) < length:
        prices = prices + [0] * (length - len(prices))
    
    # Initialize DP table
    dp = [0] * (length + 1)
    
    # Compute maximum value for each rod length
    for i in range(1, length + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            max_val = max(max_val, prices[j-1] + dp[i-j])
        dp[i] = max_val
    
    return dp[length]