def coin_change(coins, amount):
    """
    Compute the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): Available coin denominations
        amount (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make up the amount, 
             or -1 if the amount cannot be made up with given coins
    """
    # Initialize dp array with amount + 1 (max possible coins)
    # This ensures unreachable amounts are marked as impossible
    dp = [amount + 1] * (amount + 1)
    
    # Base case: 0 coins needed to make 0 amount
    dp[0] = 0
    
    # Iterate through all possible amounts from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin value is less than or equal to current amount
            if coin <= i:
                # Update minimum coins needed 
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result: minimum coins or -1 if not possible
    return dp[amount] if dp[amount] <= amount else -1