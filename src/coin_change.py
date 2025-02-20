def min_coins(coins, amount):
    """
    Find the minimum number of coins needed to make a given amount of change.
    
    Args:
        coins (list): A list of coin denominations available.
        amount (int): The target amount to make change for.
    
    Returns:
        int: Minimum number of coins needed to make the amount.
              Returns -1 if the amount cannot be made with given coins.
    
    Raises:
        ValueError: If coins list is empty or contains non-positive values.
    """
    # Validate input
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")
    if any(coin <= 0 for coin in coins):
        raise ValueError("Coin denominations must be positive")
    
    # Initialize dynamic programming array
    # dp[i] will store the minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make 0 amount
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, with -1 if amount cannot be made
    return dp[amount] if dp[amount] != float('inf') else -1