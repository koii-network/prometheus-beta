def min_coins(coins, amount):
    """
    Find the minimum number of coins needed to make a given amount of change.
    
    Args:
        coins (list): A list of available coin denominations
        amount (int): The target amount to make change for
    
    Returns:
        int: Minimum number of coins needed, or -1 if exact change is impossible
    
    Raises:
        ValueError: If coins list is empty or contains non-positive values
    """
    # Validate input
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")
    
    if any(coin <= 0 for coin in coins):
        raise ValueError("All coin denominations must be positive")
    
    # Dynamic programming solution
    # Initialize dp array with max possible value (amount + 1)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make 0 amount
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, or -1 if no solution found
    return dp[amount] if dp[amount] != float('inf') else -1