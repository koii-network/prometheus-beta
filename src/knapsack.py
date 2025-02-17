def solve_knapsack(capacity, weights, values):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
    capacity (int): Maximum weight capacity of the knapsack
    weights (list): List of weights for each item
    values (list): List of values for each item
    
    Returns:
    tuple: A tuple containing (maximum value, selected items)
    """
    # Validate inputs
    if not (len(weights) == len(values)):
        raise ValueError("Weights and values lists must have the same length")
    
    # Number of items
    n = len(weights)
    
    # Create a 2D table to store maximum values for different capacities and items
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If current item's weight is less than or equal to current capacity
            if weights[i-1] <= w:
                # Max of including or excluding the current item
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],  # Include current item
                    dp[i-1][w]  # Exclude current item
                )
            else:
                # If item's weight is more than current capacity, skip it
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find which items were selected
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    # Return maximum value and list of selected item indices
    return dp[n][capacity], list(reversed(selected_items))