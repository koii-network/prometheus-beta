def calculate_staircase_combinations(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given step lengths.
    
    :param stair_lengths: List of step lengths representing the total staircase
    :return: Number of unique ways to climb the staircase using 1 or 2 steps
    :raises ValueError: If stair_lengths is invalid
    """
    # Validate input
    if not stair_lengths:
        raise ValueError("Stair lengths list cannot be empty")
    
    if len(stair_lengths) > 100:
        raise ValueError("Staircase cannot have more than 100 steps")
    
    if any(length < 1 or length > 20 for length in stair_lengths):
        raise ValueError("Each stair length must be between 1 and 20")
    
    # Total length of the staircase
    total_length = sum(stair_lengths)
    
    # Dynamic programming array to store combinations
    dp = [0] * (total_length + 1)
    
    # Base cases
    dp[0] = 1
    
    # Iterate through possible stair lengths
    for length in range(1, total_length + 1):
        # Can climb 1 step
        if length >= 1:
            dp[length] += dp[length - 1]
        
        # Can climb 2 steps 
        if length >= 2:
            dp[length] += dp[length - 2]
    
    return min(dp[total_length], len(stair_lengths) + 1)