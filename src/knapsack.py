def solve_knapsack(capacity, weights, values):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        capacity (int): Maximum weight capacity of the knapsack
        weights (list): List of weights for each item
        values (list): List of values for each item
    
    Returns:
        tuple: A tuple containing:
            - Maximum total value that can be achieved
            - List of indices of items selected
    
    Raises:
        ValueError: If input lists have different lengths or invalid inputs
    """
    # Input validation
    if not (isinstance(capacity, int) and capacity >= 0):
        raise ValueError("Capacity must be a non-negative integer")
    
    if not (len(weights) == len(values)):
        raise ValueError("Weights and values lists must have the same length")
    
    if any(w < 0 for w in weights):
        raise ValueError("Weights must be non-negative")
    
    # Number of items
    n = len(weights)
    
    # Initialize dynamic programming table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If item can be included
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],  # Include item
                    dp[i-1][w]  # Exclude item
                )
            else:
                # Item is too heavy, cannot be included
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    # Return max value and selected items (in original order)
    return dp[n][capacity], list(reversed(selected_items))