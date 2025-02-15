def coin_change(coins, amount):
    """
    Compute the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): List of coin denominations available
        amount (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make up the amount, 
             or -1 if the amount cannot be made up with given coins
    """
    # Initialize dp array with amount+1 (impossible amount)
    # This serves as an indicator that the amount can't be made
    dp = [amount + 1] * (amount + 1)
    
    # Base case: 0 coins needed to make 0 amount
    dp[0] = 0
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin is less than or equal to current amount
            if coin <= i:
                # Update minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, or -1 if amount can't be made
    return dp[amount] if dp[amount] <= amount else -1