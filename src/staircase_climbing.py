def climb_stairs(n: int) -> int:
    """
    Calculate the number of ways to climb a staircase with n steps,
    where you can take either 1 or 2 steps at a time.
    
    Args:
        n (int): Total number of steps in the staircase
    
    Returns:
        int: Number of distinct ways to climb the stairs
    
    Raises:
        ValueError: If n is negative
    """
    # Check for invalid input
    if n < 0:
        raise ValueError("Number of steps cannot be negative")
    
    # Base cases
    if n <= 1:
        return 1
    
    # Recursive calculation with memoization
    # This prevents exponential time complexity
    memo = [0] * (n + 1)
    memo[0] = 1
    memo[1] = 1
    
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]