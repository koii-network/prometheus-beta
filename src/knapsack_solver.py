def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples, each containing (weight, value) of an item
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        int: Maximum value that can be achieved without exceeding weight capacity
    
    Raises:
        ValueError: If inputs are invalid (negative weights/capacity, non-numeric inputs)
    """
    # Input validation
    if not isinstance(capacity, (int, float)) or capacity < 0:
        raise ValueError("Capacity must be a non-negative number")
    
    if not items:
        return 0
    
    # Validate each item
    for item in items:
        if (not isinstance(item, (list, tuple)) or 
            len(item) != 2 or 
            not all(isinstance(x, (int, float)) for x in item) or 
            item[0] < 0 or 
            item[1] < 0):
            raise ValueError("Each item must be a tuple/list of (weight, value) with non-negative numbers")
    
    # Convert items to more convenient format
    weights = [item[0] for item in items]
    values = [item[1] for item in items]
    n = len(items)
    
    # Initialize DP table
    dp = [[0] * (int(capacity) + 1) for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(int(capacity) + 1):
            # If item is too heavy, skip it
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding current item
                dp[i][w] = max(
                    dp[i-1][w],  # exclude current item
                    dp[i-1][w - int(weights[i-1])] + values[i-1]  # include current item
                )
    
    # Return maximum value
    return dp[n][int(capacity)]