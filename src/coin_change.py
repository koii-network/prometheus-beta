def coin_change(coins, amount):
    """
    Compute the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): A list of coin denominations available
        amount (int): The target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make up the amount, 
             or -1 if the amount cannot be made up by the given coins
    
    Raises:
        TypeError: If amount is not an integer
    """
    # Validate input
    if not isinstance(amount, int):
        raise TypeError("Amount must be an integer")
    
    if amount < 0:
        raise TypeError("Amount cannot be negative")
    
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")
    
    if any(coin <= 0 for coin in coins):
        raise ValueError("All coin denominations must be positive")
    
    # Special case: if amount is 0, no coins needed
    if amount == 0:
        return 0
    
    # Sort coins in descending order for greedy approach
    coins = sorted(coins, reverse=True)
    
    # Initialize dynamic programming array
    # Set to a large value (amount + 1) which is larger than max possible coins
    dp = [float('inf')] * (amount + 1)
    
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
    return dp[amount] if dp[amount] != float('inf') else -1