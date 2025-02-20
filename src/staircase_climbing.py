def climb_stairs(n):
    """
    Calculate the number of ways to climb a staircase using 1 or 2 steps.
    
    Args:
        n (int): Total number of steps in the staircase.
    
    Returns:
        int: Number of distinct ways to climb the stairs.
    
    Raises:
        ValueError: If the input is negative.
    """
    # Check for invalid input
    if n < 0:
        raise ValueError("Number of steps must be non-negative")
    
    # Base cases
    if n <= 1:
        return 1
    
    # Recursive solution with memoization
    memo = [0] * (n + 1)
    memo[0] = 1
    memo[1] = 1
    
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]