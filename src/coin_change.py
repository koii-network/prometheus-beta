def coin_change(coins, amount):
    """
    Compute the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): Available coin denominations
        amount (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make up the amount
             Returns -1 if the amount cannot be made up by given coins
    """
    # Initialize dynamic programming array with a large value
    # Large value is amount + 1 as maximum possible coins would be amount itself
    dp = [amount + 1] * (amount + 1)
    
    # Base case: 0 coins needed to make 0 amount
    dp[0] = 0
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= i:
                # Update minimum coins needed for current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result: -1 if amount can't be made, else minimum coins
    return dp[amount] if dp[amount] <= amount else -1