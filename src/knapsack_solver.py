def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples, where each tuple contains (weight, value)
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        int: Maximum value that can be achieved without exceeding weight capacity
    
    Raises:
        ValueError: If inputs are invalid
    """
    # Input validation
    if not isinstance(items, list):
        raise ValueError("Items must be a list of (weight, value) tuples")
    
    if not isinstance(capacity, int) or capacity < 0:
        raise ValueError("Capacity must be a non-negative integer")
    
    # Handle empty input cases
    if not items or capacity == 0:
        return 0
    
    # Validate individual items
    for item in items:
        if not (isinstance(item, tuple) and len(item) == 2 and 
                isinstance(item[0], (int, float)) and isinstance(item[1], (int, float)) and
                item[0] >= 0 and item[1] >= 0):
            raise ValueError("Each item must be a tuple of (weight, value) with non-negative numbers")
    
    # Number of items
    n = len(items)
    
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        weight, value = items[i-1]
        
        for w in range(1, capacity + 1):
            # If item can be included
            if weight <= w:
                dp[i][w] = max(
                    value + dp[i-1][w-weight],  # Include current item
                    dp[i-1][w]                  # Exclude current item
                )
            else:
                # Cannot include current item
                dp[i][w] = dp[i-1][w]
    
    # Return maximum value
    return dp[n][capacity]