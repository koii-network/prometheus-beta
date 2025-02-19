def solve_knapsack(items, max_weight):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples, where each tuple contains (weight, value)
        max_weight (int): Maximum weight capacity of the knapsack
    
    Returns:
        tuple: A tuple containing (max_value, selected_items)
               - max_value: Total value of the most valuable combination
               - selected_items: List of indices of items selected
    """
    # Number of items
    n = len(items)
    
    # Create a 2D table for dynamic programming
    # dp[i][w] represents max value for first i items with weight limit w
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    # Build the dynamic programming table
    for i in range(1, n + 1):
        item_weight, item_value = items[i-1]
        
        for w in range(max_weight + 1):
            # If we can't include the current item
            if item_weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding the current item
                dp[i][w] = max(
                    dp[i-1][w],  # exclude current item
                    dp[i-1][w-item_weight] + item_value  # include current item
                )
    
    # Backtrack to find selected items
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= items[i-1][0]
    
    # Reverse to maintain original order
    selected_items.reverse()
    
    return dp[n][max_weight], selected_items