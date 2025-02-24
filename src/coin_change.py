def min_coins(coins, amount):
    """
    Find the minimum number of coins needed to make a given amount of change.
    
    Args:
        coins (list): A list of available coin denominations.
        amount (int): The target amount to make change for.
    
    Returns:
        int: The minimum number of coins needed to make the amount.
             Returns -1 if the amount cannot be made with the given coins.
    
    Raises:
        ValueError: If coins list is empty or contains non-positive values.
        TypeError: If inputs are not of the correct type.
    
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    # Input validation
    if not isinstance(coins, list):
        raise TypeError("Coins must be a list of integers")
    if not isinstance(amount, int):
        raise TypeError("Amount must be an integer")
    
    # Check for empty or invalid coin list
    if not coins:
        raise ValueError("Coin list cannot be empty")
    
    # Check for non-positive coin values
    if any(coin <= 0 for coin in coins):
        raise ValueError("All coin denominations must be positive")
    
    # Special case: amount is 0
    if amount == 0:
        return 0
    
    # Sort coins in descending order for greedy approach
    coins = sorted(coins, reverse=True)
    
    # Initialize coin count and remaining amount
    total_coins = 0
    remaining = amount
    
    # Greedy coin selection
    for coin in coins:
        # Use as many of the current coin as possible
        num_coins = remaining // coin
        total_coins += num_coins
        remaining -= num_coins * coin
    
    # Check if exact change was made
    return total_coins if remaining == 0 else -1