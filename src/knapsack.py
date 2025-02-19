def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples (weight, value) representing items
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        int: Maximum value that can be achieved without exceeding weight capacity
    """
    # Validate inputs
    if not items or capacity < 0:
        return 0
    
    # Create a 2D dynamic programming table
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build the table bottom-up
    for i in range(1, n + 1):
        weight, value = items[i-1]
        
        for w in range(capacity + 1):
            # If we don't include the current item
            dp[i][w] = dp[i-1][w]
            
            # If we can include the current item
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + value)
    
    # Return the maximum value
    return dp[n][capacity]