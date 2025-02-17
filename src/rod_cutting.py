def rod_cutting(prices, n):
    """
    Solve the Rod Cutting problem using dynamic programming.
    
    Args:
    prices (list): A list of prices for rod lengths from 1 to len(prices)
    n (int): The length of the rod to be cut
    
    Returns:
    int: The maximum obtainable value by cutting the rod
    list: The optimal cutting strategy
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    # Validate inputs
    if not prices or n <= 0:
        return 0, []
    
    # Extend prices list if n is larger than available prices
    if n > len(prices):
        prices = prices + [0] * (n - len(prices))
    
    # Initialize dynamic programming arrays
    max_value = [0] * (n + 1)
    split_points = [0] * (n + 1)
    
    # Fill the dynamic programming table
    for i in range(1, n + 1):
        max_current = float('-inf')
        for j in range(1, i + 1):
            # Check if cutting at length j gives a better value
            current_value = prices[j - 1] + max_value[i - j]
            if current_value > max_current:
                max_current = current_value
                split_points[i] = j
        max_value[i] = max_current
    
    # Reconstruct the cutting strategy
    cutting_strategy = []
    remaining_length = n
    while remaining_length > 0:
        cut_length = split_points[remaining_length]
        cutting_strategy.append(cut_length)
        remaining_length -= cut_length
    
    return max_value[n], cutting_strategy