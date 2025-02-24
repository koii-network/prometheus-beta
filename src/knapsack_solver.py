def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples, where each tuple contains (weight, value)
        capacity (int or float): Maximum weight capacity of the knapsack
    
    Returns:
        float: Maximum value that can be achieved without exceeding weight capacity
    
    Raises:
        ValueError: If inputs are invalid
    """
    # Input validation
    if not isinstance(items, list):
        raise ValueError("Items must be a list of (weight, value) tuples")
    
    if not isinstance(capacity, (int, float)) or capacity < 0:
        raise ValueError("Capacity must be a non-negative number")
    
    # Convert capacity to integer, multiplying by 100 to preserve precision
    int_capacity = int(float(capacity) * 100)
    
    # Handle empty input cases
    if not items or int_capacity == 0:
        return 0.0
    
    # Validate individual items
    processed_items = []
    for item in items:
        if not (isinstance(item, tuple) and len(item) == 2 and 
                isinstance(item[0], (int, float)) and isinstance(item[1], (int, float)) and
                item[0] >= 0 and item[1] >= 0):
            raise ValueError("Each item must be a tuple of (weight, value) with non-negative numbers")
        
        # Convert weights and values to integers by multiplying by 100
        processed_items.append((int(float(item[0]) * 100), float(item[1])))
    
    # Number of items
    n = len(processed_items)
    
    # Create DP table
    dp = [[0.0 for _ in range(int_capacity + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        weight, value = processed_items[i-1]
        
        for w in range(1, int_capacity + 1):
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
    return round(dp[n][int_capacity], 2)