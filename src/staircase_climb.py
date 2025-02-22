def calculate_climb_combinations(stair_lengths):
    """
    Calculate the number of ways to climb a staircase given stair lengths.
    
    You can climb either 1 or 2 steps at a time.
    
    Args:
        stair_lengths (list): A list of integers representing the lengths of stairs.
    
    Returns:
        int: Number of unique ways to climb the entire staircase.
    
    Raises:
        ValueError: If stair_lengths is empty or contains non-positive integers.
    """
    # Validate input
    if not stair_lengths:
        raise ValueError("Stair lengths list cannot be empty")
    
    if any(length <= 0 for length in stair_lengths):
        raise ValueError("All stair lengths must be positive integers")
    
    # Total length of the staircase
    total_length = sum(stair_lengths)
    
    # Dynamic programming to calculate combinations
    dp = [0] * (total_length + 1)
    dp[0] = 1  # Base case: one way to climb zero stairs
    
    # Calculate combinations
    for length in range(1, total_length + 1):
        # Can climb 1 step
        if length >= 1:
            dp[length] += dp[length - 1]
        
        # Can climb 2 steps 
        if length >= 2:
            dp[length] += dp[length - 2]
    
    return dp[total_length]