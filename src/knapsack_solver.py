def solve_knapsack(weights, values, capacity):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        weights (list): List of item weights
        values (list): List of item values
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        tuple: A tuple containing (max_value, selected_items)
            - max_value (int): Maximum total value that can be carried
            - selected_items (list): Indices of items selected
    
    Raises:
        ValueError: If input lists have different lengths or invalid inputs
    """
    # Input validation
    if len(weights) != len(values):
        raise ValueError("Weights and values lists must have equal length")
    
    if capacity < 0:
        raise ValueError("Knapsack capacity must be non-negative")
    
    n = len(weights)
    
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't include the current item
            dp[i][w] = dp[i-1][w]
            
            # Check if including the current item yields a better value
            if weights[i-1] <= w:
                candidate_value = dp[i-1][w - weights[i-1]] + values[i-1]
                dp[i][w] = max(dp[i][w], candidate_value)
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    selected_items.reverse()
    
    return dp[n][capacity], selected_items