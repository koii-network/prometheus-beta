def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.
    
    Args:
        n (int): A non-negative integer to calculate factorial for.
    
    Returns:
        int: The factorial of the input number.
    
    Raises:
        ValueError: If input is negative.
        TypeError: If input is not an integer.
    """
    # Type checking
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Negative input check
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive calculation
    return n * factorial(n - 1)