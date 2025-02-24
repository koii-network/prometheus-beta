def count_staircase_combinations(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given stair lengths.
    
    Args:
        stair_lengths (list): A list of integers representing the total stair lengths 
                               for which to calculate climbing combinations.
    
    Returns:
        list: A list of integers representing the number of ways to climb each staircase.
    
    Raises:
        ValueError: If the input is not a list or contains non-positive integers.
    """
    # Input validation
    if not isinstance(stair_lengths, list):
        raise ValueError("Input must be a list of integers")
    
    if any(not isinstance(n, int) or n < 0 for n in stair_lengths):
        raise ValueError("All stair lengths must be non-negative integers")
    
    # Function to calculate combinations for a single staircase
    def count_single_staircase(n):
        # Handle base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Dynamic programming solution
        # dp[i] represents the number of ways to climb to step i
        dp = [0] * (n + 1)
        dp[1] = 1  # One way to climb 1 step
        dp[2] = 2  # Two ways to climb 2 steps (1+1 or 2)
        
        # Build up the combinations
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    # Calculate combinations for each stair length
    return [count_single_staircase(length) for length in stair_lengths]