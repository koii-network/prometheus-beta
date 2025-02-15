def rod_cutting(prices, rod_length):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
        prices (list): A list of prices for rod lengths from 1 to len(prices)
        rod_length (int): The total length of the rod to be cut
    
    Returns:
        tuple: A tuple containing (max_revenue, cutting_strategy)
               max_revenue is the maximum obtainable revenue
               cutting_strategy is a list of piece lengths that maximize revenue
    
    Raises:
        ValueError: If input is invalid
    """
    # Input validation
    if not prices or rod_length <= 0:
        return 0, []
    
    if rod_length > len(prices):
        prices.extend([0] * (rod_length - len(prices)))
    
    # Dynamic programming to find max revenue
    dp = [0] * (rod_length + 1)
    cuts = [[] for _ in range(rod_length + 1)]
    
    for length in range(1, rod_length + 1):
        max_val = float('-inf')
        best_cut = []
        
        for cut_length in range(1, length + 1):
            # Check revenue if we make a cut of this length
            current_revenue = prices[cut_length - 1] + dp[length - cut_length]
            
            if current_revenue > max_val:
                max_val = current_revenue
                best_cut = cuts[length - cut_length] + [cut_length]
        
        dp[length] = max_val
        cuts[length] = best_cut
    
    return dp[rod_length], cuts[rod_length]