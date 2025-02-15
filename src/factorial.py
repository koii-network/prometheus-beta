def calculate_factorial(n):
    """
    Calculate the factorial of a given non-negative integer.
    
    Args:
        n (int): A non-negative integer for which factorial will be calculated.
    
    Returns:
        int: The factorial of the input number.
    
    Raises:
        ValueError: If the input is a negative number.
        TypeError: If the input is not an integer.
    """
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base case: 0! and 1! are 1
    if n <= 1:
        return 1
    
    # Recursive calculation of factorial
    return n * calculate_factorial(n - 1)