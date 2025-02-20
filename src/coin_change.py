def min_coins(amount, coins):
    """
    Find the minimum number of coins needed to make a given amount of change.
    
    Args:
        amount (int): The target amount to make change for
        coins (list): List of available coin denominations
    
    Returns:
        int: Minimum number of coins needed, or -1 if exact change is impossible
    """
    # Handle invalid inputs
    if amount < 0 or not coins:
        return -1
    
    # Initialize dynamic programming array
    # Set initial values to a large number (impossible to reach)
    dp = [float('inf')] * (amount + 1)
    
    # Base case: 0 coins needed to make 0 amount
    dp[0] = 0
    
    # Iterate through all possible amounts from 1 to target amount
    for current_amount in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin is less than or equal to current amount
            if coin <= current_amount:
                # Update minimum number of coins needed
                dp[current_amount] = min(
                    dp[current_amount], 
                    dp[current_amount - coin] + 1
                )
    
    # Return result, using -1 if no solution was found
    return dp[amount] if dp[amount] != float('inf') else -1