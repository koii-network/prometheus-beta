def coin_change(coins, amount):
    """
    Compute the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): List of coin denominations available
        amount (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make up the amount, 
             or -1 if the amount cannot be made up exactly
    
    Raises:
        TypeError: If coins is not a list or amount is not an integer
        ValueError: If amount is negative or coins contain negative values
    """
    # Input validation
    if not isinstance(coins, list):
        raise TypeError("Coins must be a list")
    if not isinstance(amount, int):
        raise TypeError("Amount must be an integer")
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("Coins must be positive integers")
    
    # Special case for empty coins list
    if not coins:
        return -1
    
    # Initialize dp array with amount + 1 (max possible coins)
    dp = [amount + 1] * (amount + 1)
    
    # 0 coins needed to make 0 amount
    dp[0] = 0
    
    # Iterate through all amounts from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin is less than or equal to current amount
            if coin <= i:
                # Update minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, or -1 if amount cannot be made
    return dp[amount] if dp[amount] <= amount else -1