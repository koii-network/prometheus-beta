def min_coins(coins, amount):
    """
    Find the minimum number of coins needed to make a given amount of change.
    
    Args:
        coins (list): List of available coin denominations
        amount (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make the amount
             Returns -1 if the amount cannot be made with given coins
    """
    # Initialize dp array with max value (amount + 1) 
    # representing an impossible number of coins
    dp = [float('inf')] * (amount + 1)
    
    # 0 coins needed to make 0 amount
    dp[0] = 0
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= i:
                # Update minimum coins needed if using this coin reduces total
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return minimum coins or -1 if amount cannot be made
    return dp[amount] if dp[amount] != float('inf') else -1