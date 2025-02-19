def solve_knapsack(items, max_weight):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
    - items (list): A list of tuples (weight, value) representing items
    - max_weight (int): Maximum weight capacity of the knapsack
    
    Returns:
    - tuple: A tuple containing (max_value, selected_items)
        - max_value (int): Maximum total value of items that can be carried
        - selected_items (list): List of indices of items selected
    """
    # Validate inputs
    if not items or max_weight < 0:
        return 0, []
    
    # Number of items
    n = len(items)
    
    # Create DP table
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(max_weight + 1):
            # If item can't be included due to weight
            if weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding the item
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
    
    # Backtrack to find selected items
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= items[i-1][0]
    
    # Return max value and list of selected item indices (in reverse order)
    return dp[n][max_weight], list(reversed(selected_items))