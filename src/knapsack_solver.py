def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples, where each tuple contains (weight, value)
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        int: Maximum value that can be achieved without exceeding weight capacity
    
    Raises:
        ValueError: If input is invalid (negative weights/capacity or non-numeric inputs)
    """
    # Input validation
    if capacity < 0:
        raise ValueError("Knapsack capacity must be non-negative")
    
    if not items:
        return 0
    
    # Validate each item
    for weight, value in items:
        if weight < 0 or value < 0:
            raise ValueError("Item weights and values must be non-negative")
    
    # Initialize dynamic programming table
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build the dp table
    for i in range(1, n + 1):
        item_weight, item_value = items[i-1]
        
        for w in range(capacity + 1):
            # Don't take the item
            dp[i][w] = dp[i-1][w]
            
            # Take the item if it fits
            if item_weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-item_weight] + item_value)
    
    # Return the maximum value
    return dp[n][capacity]