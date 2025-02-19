def calculate_climbing_ways(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given stair lengths.
    
    Args:
        stair_lengths (list): A list of integers representing stair lengths.
    
    Returns:
        int: Number of ways to climb the staircase by taking 1 or 2 steps at a time.
    
    Raises:
        ValueError: If stair_lengths is empty or contains non-positive values.
    """
    # Input validation
    if not stair_lengths:
        raise ValueError("Stair lengths cannot be empty")
    
    if any(length <= 0 for length in stair_lengths):
        raise ValueError("All stair lengths must be positive")
    
    # Total length of the staircase
    total_length = sum(stair_lengths)
    
    # Dynamic programming to calculate climbing ways
    dp = [0] * (total_length + 1)
    dp[0] = 1  # Base case: one way to climb 0 steps
    
    for i in range(1, total_length + 1):
        # Can climb 1 step
        if i >= 1:
            dp[i] += dp[i - 1]
        
        # Can climb 2 steps
        if i >= 2:
            dp[i] += dp[i - 2]
    
    return dp[total_length]