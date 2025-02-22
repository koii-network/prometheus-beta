def solve_knapsack(capacity, weights, values):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        capacity (int): Maximum weight capacity of the knapsack
        weights (list): List of weights for each item
        values (list): List of values for each item
    
    Returns:
        tuple: A tuple containing (max_value, selected_items)
               max_value (int): Maximum value that can be achieved
               selected_items (list): Indices of items selected
    
    Raises:
        ValueError: If input lists have different lengths or invalid inputs
    """
    # Input validation
    if len(weights) != len(values):
        raise ValueError("Weights and values lists must have the same length")
    
    if capacity < 0:
        raise ValueError("Knapsack capacity must be non-negative")
    
    n = len(weights)
    
    # Create a 2D table for dynamic programming
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                # Max of including or excluding the current item
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]], 
                    dp[i-1][w]
                )
            else:
                # Cannot include current item
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    selected_items.reverse()
    
    return dp[n][capacity], selected_items