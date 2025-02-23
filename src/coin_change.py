def min_coins(coins, amount):
    """
    Find the minimum number of coins needed to make a given amount of change.
    
    Args:
        coins (list): A list of coin denominations available
        amount (int): The target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make the amount, 
             or -1 if the amount cannot be made exactly
    """
    # Handle invalid inputs
    if amount < 0 or not coins:
        return -1
    
    # Initialize dynamic programming table
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
    
    # Return result, or -1 if amount cannot be made
    return dp[amount] if dp[amount] != float('inf') else -1