def min_coins(amount, coins):
    """
    Find the minimum number of coins needed to make a given amount of change.
    
    Args:
        amount (int): The target amount of change to make.
        coins (list): A list of available coin denominations.
    
    Returns:
        int: The minimum number of coins needed to make the amount.
             Returns -1 if the amount cannot be made with given coins.
    
    Raises:
        ValueError: If amount is negative or coins list is empty.
    """
    # Validate input
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    if not coins:
        raise ValueError("Coins list cannot be empty")
    
    # Initialize dynamic programming array
    # dp[i] will store the minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make 0 amount
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= i:
                # Update minimum coins if using this coin leads to fewer total coins
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, using -1 if amount cannot be made
    return dp[amount] if dp[amount] != float('inf') else -1