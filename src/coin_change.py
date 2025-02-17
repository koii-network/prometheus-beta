def coin_change(coins, amount):
    """
    Compute the minimum number of coins needed to make a specific amount.
    
    Args:
        coins (list): List of coin denominations available
        amount (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make the amount, 
             or -1 if the amount cannot be made with given coins
    """
    # Initialize dynamic programming array
    # Set initial values to a large number (amount + 1)
    dp = [amount + 1] * (amount + 1)
    
    # Base case: 0 coins needed to make 0 amount
    dp[0] = 0
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= i:
                # Update minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, -1 if amount cannot be made
    return dp[amount] if dp[amount] <= amount else -1