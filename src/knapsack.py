def solve_knapsack(capacity, weights, values):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        capacity (int): Maximum weight capacity of the knapsack
        weights (list): List of weights for each item
        values (list): List of values for each item
    
    Returns:
        tuple: A tuple containing (max_value, selected_items)
            - max_value (int): Maximum total value that can be carried
            - selected_items (list): Indices of items selected to maximize value
    
    Raises:
        ValueError: If input lists have different lengths or invalid inputs
    """
    # Input validation
    if not (len(weights) == len(values)):
        raise ValueError("Weights and values lists must have the same length")
    
    if capacity < 0:
        raise ValueError("Knapsack capacity must be non-negative")
    
    n = len(weights)
    
    # Handle empty list case
    if n == 0:
        return 0, []
    
    # Dynamic programming table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If current item's weight exceeds capacity, skip it
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding current item
                dp[i][w] = max(
                    dp[i-1][w],  # Exclude item
                    dp[i-1][w - weights[i-1]] + values[i-1]  # Include item
                )
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i - 1)
            w -= weights[i-1]
    
    selected_items.reverse()
    
    return dp[n][capacity], selected_items