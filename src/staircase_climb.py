def climb_stairs(n):
    """
    Calculate the number of ways to climb a staircase with 1 or 2 steps at a time.
    
    Args:
        n (int): Total number of steps in the staircase
    
    Returns:
        int: Number of unique ways to climb the staircase
    
    Raises:
        ValueError: If n is negative
    """
    # Handle invalid input
    if n < 0:
        raise ValueError("Number of steps must be non-negative")
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: sum of ways to climb from previous two steps
    return climb_stairs(n-1) + climb_stairs(n-2)