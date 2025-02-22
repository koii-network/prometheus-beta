def solve_knapsack(items, max_weight):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples (weight, value) representing items
        max_weight (int): Maximum weight capacity of the knapsack
    
    Returns:
        tuple: A tuple containing (max_value, selected_items)
            - max_value (int): Maximum total value of selected items
            - selected_items (list): List of indices of selected items
    """
    # Validate inputs
    if not items or max_weight < 0:
        return 0, []
    
    n = len(items)
    # Create a 2D DP table
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(max_weight + 1):
            # Don't include current item
            dp[i][w] = dp[i-1][w]
            
            # Try to include current item if possible
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + value)
    
    # Trace back to find selected items
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= items[i-1][0]
    
    return dp[n][max_weight], list(reversed(selected_items))