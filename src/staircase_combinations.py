def calculate_staircase_combinations(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given step lengths.
    
    Args:
        stair_lengths (list): A list of integers representing the lengths of stairs.
    
    Returns:
        int: The total number of unique ways to climb the staircase.
    
    Raises:
        ValueError: If the input is not a valid list of positive integers.
    """
    # Validate input
    if not isinstance(stair_lengths, list):
        raise ValueError("Input must be a list of integers")
    
    if not all(isinstance(length, int) and length > 0 for length in stair_lengths):
        raise ValueError("All stair lengths must be positive integers")
    
    # Total length of the staircase
    total_length = sum(stair_lengths)
    
    # Dynamic programming to calculate combinations
    # dp[i] represents the number of ways to reach step i
    dp = [0] * (total_length + 1)
    
    # Base cases
    dp[0] = 1  # There's one way to climb 0 steps (do nothing)
    
    # Iterate through possible steps
    for length in stair_lengths:
        for i in range(length, total_length + 1):
            # Can climb 1 or 2 steps at a time
            dp[i] += dp[i - 1] if i - 1 >= 0 else 0
            dp[i] += dp[i - 2] if i - 2 >= 0 else 0
    
    return dp[total_length]