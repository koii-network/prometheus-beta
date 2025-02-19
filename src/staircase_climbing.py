def count_climbing_ways(stair_lengths):
    """
    Calculate the number of ways to climb a staircase given stair lengths.
    
    Args:
        stair_lengths (list): A list of stair lengths to climb
    
    Returns:
        int: Number of unique ways to climb the staircase using 1 or 2 steps
    
    Raises:
        ValueError: If input is not a valid list of positive integers
    """
    # Input validation
    if not stair_lengths or not isinstance(stair_lengths, list):
        raise ValueError("Input must be a non-empty list of stair lengths")
    
    if any(not isinstance(length, int) or length <= 0 for length in stair_lengths):
        raise ValueError("All stair lengths must be positive integers")
    
    # Total staircase length
    total_length = sum(stair_lengths)
    
    # Dynamic programming solution
    dp = [0] * (total_length + 1)
    dp[0] = 1  # Base case: one way to climb 0 stairs
    
    # Pre-calculate valid step lengths 
    valid_steps = [1, 2]
    
    # Build the dynamic programming table
    for i in range(1, total_length + 1):
        for step in valid_steps:
            if i >= step:
                dp[i] += dp[i - step]
    
    return dp[total_length]