def calculate_staircase_combinations(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given step lengths.
    
    You can climb 1 or 2 steps at a time.
    
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
    
    # If no stairs, there's one way to do nothing
    if total_length == 0:
        return 1
    
    # Dynamic programming to calculate combinations
    # dp[i] represents the number of ways to reach step i
    dp = [0] * (total_length + 1)
    
    # Base cases
    dp[0] = 1  # One way to climb 0 steps
    
    # Climb up to the total length
    for i in range(1, total_length + 1):
        # Add ways from 1-step and 2-step climbs, if possible
        dp[i] = dp[i - 1] if i >= 1 else 0
        dp[i] += dp[i - 2] if i >= 2 else 0
    
    return dp[total_length]