def has_arithmetic_progression(arr):
    """
    Determine if any three consecutive numbers in the array form an arithmetic progression.
    
    An arithmetic progression is a sequence of numbers where the difference 
    between consecutive terms is constant.
    
    Args:
        arr (list): A list of positive integers.
    
    Returns:
        bool: True if any three consecutive numbers form an arithmetic progression, 
              False otherwise.
    
    Raises:
        ValueError: If the input is not a list or contains non-positive integers.
    
    Examples:
        >>> has_arithmetic_progression([1, 2, 3, 4, 5])  # True (1,2,3 or 2,3,4 or 3,4,5)
        True
        >>> has_arithmetic_progression([1, 3, 5, 7, 9])  # True (1,3,5 or 3,5,7 or 5,7,9)
        True
        >>> has_arithmetic_progression([1, 2, 4, 8, 16])  # False
        False
        >>> has_arithmetic_progression([])  # False (too few elements)
        False
    """
    # Validate input
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    # Check for non-positive integers or non-integers
    if any(not isinstance(x, int) or x <= 0 for x in arr):
        raise ValueError("All elements must be positive integers")
    
    # Not enough elements to form a progression
    if len(arr) < 3:
        return False
    
    # Check every consecutive triplet
    for i in range(len(arr) - 2):
        # Check if the three consecutive numbers form an arithmetic progression
        # An arithmetic progression means b - a = c - b
        a, b, c = arr[i], arr[i+1], arr[i+2]
        if b - a == c - b:
            return True
    
    return False