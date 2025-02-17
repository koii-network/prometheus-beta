def rod_cutting(prices, n):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
    prices (list): List of prices for rod lengths from 1 to len(prices)
    n (int): Length of the rod to cut
    
    Returns:
    int: Maximum obtainable value by cutting the rod
    list: Cutting strategy (lengths of pieces)
    """
    # Validate inputs
    if not prices or n <= 0:
        return 0, []
    
    # Extend prices list if n is larger than original prices list
    if n > len(prices):
        prices = prices + [0] * (n - len(prices))
    
    # Dynamic programming solution
    # dp[i] will store the maximum value obtainable for a rod of length i
    dp = [0] * (n + 1)
    
    # Keep track of cuts
    cuts = [[] for _ in range(n + 1)]
    
    # Build solution bottom-up
    for i in range(1, n + 1):
        max_val = float('-inf')
        best_cut = []
        
        # Try all possible first cuts
        for j in range(1, i + 1):
            # Value of current cut + optimal solution for remaining length
            current_val = prices[j-1] + dp[i-j]
            
            if current_val > max_val:
                max_val = current_val
                # Construct cutting strategy
                best_cut = cuts[i-j] + [j]
        
        dp[i] = max_val
        cuts[i] = best_cut
    
    return dp[n], cuts[n]