def climb_stairs(n: int) -> int:
    """
    Calculate the number of unique ways to climb a staircase.
    
    This recursive function with memoization determines the number of distinct 
    ways to climb a staircase, where you can take either 1 or 2 steps at a time.
    
    Args:
        n (int): Total number of steps in the staircase. Must be non-negative.
    
    Returns:
        int: Number of unique ways to climb the staircase.
    
    Raises:
        ValueError: If the input is negative.
        TypeError: If the input is not an integer.
    
    Examples:
        >>> climb_stairs(2)
        2
        >>> climb_stairs(3)
        3
        >>> climb_stairs(0)
        1
    """
    # Check for valid input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check for invalid input
    if n < 0:
        raise ValueError("Number of steps must be non-negative")
    
    # Memoization cache to store already computed results
    memo = {}
    
    def _climb_recursive(steps: int) -> int:
        # Base cases
        if steps <= 1:
            return 1
        
        # Check if result is already memoized
        if steps in memo:
            return memo[steps]
        
        # Recursive calculation: ways to climb = ways to climb (n-1) + ways to climb (n-2)
        memo[steps] = _climb_recursive(steps - 1) + _climb_recursive(steps - 2)
        return memo[steps]
    
    return _climb_recursive(n)