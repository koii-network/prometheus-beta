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
    
    # Number of items
    n = len(items)
    
    # Create a 2D DP table 
    # Rows represent items, columns represent weights from 0 to capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Current item's weight and value
            weight, value = items[i-1]
            
            # If item can't be included due to weight constraint
            if weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding current item
                dp[i][w] = max(
                    value + dp[i-1][w-weight],  # Include current item
                    dp[i-1][w]                  # Exclude current item
                )
    
    # Return maximum value
    return dp[n][capacity]