def min_coins(coins, amount):
    """
    Calculate the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): A list of available coin denominations (positive integers)
        amount (int): The target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make up the amount
             Returns -1 if the amount cannot be made up exactly
    
    Raises:
        ValueError: If coins list is empty or contains non-positive values
    """
    # Validate input
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")
    
    if any(coin <= 0 for coin in coins):
        raise ValueError("All coin denominations must be positive integers")
    
    # Handle base cases
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    
    # Initialize dynamic programming array
    # Set max value to amount + 1 to represent "impossible"
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= i:
                # Update minimum coins needed if using this coin leads to fewer coins
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, with -1 if amount cannot be made exactly
    return dp[amount] if dp[amount] <= amount else -1