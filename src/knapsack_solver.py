def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples, where each tuple contains (weight, value) 
                      of an item. Each item can be included at most once.
        capacity (int): Maximum weight capacity of the knapsack.
    
    Returns:
        int: Maximum value that can be achieved without exceeding weight capacity.
    
    Raises:
        ValueError: If inputs are invalid (negative weights/capacity, non-numeric inputs)
    """
    # Input validation
    if not isinstance(capacity, (int, float)) or capacity < 0:
        raise ValueError("Capacity must be a non-negative number")
    
    if not items:
        return 0
    
    # Validate each item
    for weight, value in items:
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Item weights must be non-negative numbers")
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Item values must be non-negative numbers")
    
    # Cast capacity to int to handle float inputs
    capacity = int(capacity)
    
    # Dynamic programming table
    # dp[i] represents the maximum value achievable with capacity i
    dp = [0] * (capacity + 1)
    
    # Compute maximum value for each possible capacity
    for weight, value in items:
        # We traverse backwards to avoid using the same item multiple times
        for j in range(capacity, int(weight) - 1, -1):
            dp[j] = max(dp[j], dp[j - int(weight)] + value)
    
    # Return the maximum value achievable
    return dp[capacity]