def knapsack(max_weight, weights, values):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    :param max_weight: Maximum weight capacity of the knapsack
    :param weights: List of weights for each item
    :param values: List of values for each item
    :return: Maximum total value that can be achieved without exceeding max_weight
    """
    # Validate input
    if len(weights) != len(values):
        raise ValueError("Weights and values lists must have the same length")
    
    # Number of items
    n = len(weights)
    
    # Create a 2D table to store maximum values
    # dp[i][w] represents max value for first i items with weight limit w
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            # Current item's weight and value
            current_weight = weights[i-1]
            current_value = values[i-1]
            
            # If current item can be included
            if current_weight <= w:
                # Max of including or excluding current item
                dp[i][w] = max(
                    current_value + dp[i-1][w-current_weight],  # Include current item
                    dp[i-1][w]  # Exclude current item
                )
            else:
                # Cannot include current item, copy previous row's value
                dp[i][w] = dp[i-1][w]
    
    # Maximum value will be in the bottom-right cell
    return dp[n][max_weight]