def has_arithmetic_progression(arr):
    """
    Determines if any three consecutive numbers in the array form an arithmetic progression.
    
    An arithmetic progression is a sequence where the difference between consecutive terms is constant.
    
    Args:
    arr (list): A list of positive integers
    
    Returns:
    bool: True if any three consecutive numbers form an arithmetic progression, False otherwise
    
    Raises:
    ValueError: If the input is not a list or contains non-positive integers
    """
    # Input validation
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    if not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("All elements must be positive integers")
    
    # Check for arithmetic progression
    for i in range(len(arr) - 2):
        # Check if three consecutive numbers form an arithmetic progression
        if arr[i+1] - arr[i] == arr[i+2] - arr[i+1]:
            return True
    
    return False