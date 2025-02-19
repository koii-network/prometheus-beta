def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
    - items (list of dict): List of items, where each item is a dictionary 
      with 'weight' and 'value' keys
    - capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
    - int: Maximum value that can be achieved without exceeding weight capacity
    
    Raises:
    - ValueError: If items is not a list or capacity is not a non-negative integer
    """
    # Input validation
    if not isinstance(items, list):
        raise ValueError("Items must be a list of dictionaries")
    
    if not isinstance(capacity, int) or capacity < 0:
        raise ValueError("Capacity must be a non-negative integer")
    
    # If no items or zero capacity, return 0
    if not items or capacity == 0:
        return 0
    
    # Create a 2D table to store maximum values
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Current item's weight and value
            item_weight = items[i-1]['weight']
            item_value = items[i-1]['value']
            
            # If item can be included
            if item_weight <= w:
                # Max of including or excluding current item
                dp[i][w] = max(
                    dp[i-1][w],  # Exclude current item
                    dp[i-1][w-item_weight] + item_value  # Include current item
                )
            else:
                # Item too heavy, exclude it
                dp[i][w] = dp[i-1][w]
    
    # Return maximum value possible
    return dp[n][capacity]