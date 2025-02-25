def count_climbing_ways(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given stair lengths.
    
    The climber can take 1 or 2 steps at a time, and must exactly reach the top.
    
    Args:
        stair_lengths (list): A list of integers representing the total length 
                               of each staircase to climb.
    
    Returns:
        list: Number of distinct ways to climb each staircase.
    
    Raises:
        ValueError: If input is not a list or contains non-positive integers.
    """
    # Input validation
    if not isinstance(stair_lengths, list):
        raise ValueError("Input must be a list of stair lengths")
    
    if any(not isinstance(length, int) or length <= 0 for length in stair_lengths):
        raise ValueError("Stair lengths must be positive integers")
    
    # Function to calculate ways for a single staircase
    def climb_ways(n):
        # Base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Dynamic programming approach
        # dp[i] represents the number of ways to climb i stairs
        dp = [0] * (n + 1)
        dp[1] = 1  # One way to climb 1 stair
        dp[2] = 2  # Two ways to climb 2 stairs (1+1 or 2)
        
        # Build solution bottom-up
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    # Calculate ways for each staircase length
    return [climb_ways(length) for length in stair_lengths]