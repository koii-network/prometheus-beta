def multiply(arr1, arr2):
    """
    Multiply corresponding elements of two input arrays.
    
    Args:
        arr1 (list): First input array of numbers
        arr2 (list): Second input array of numbers
    
    Returns:
        list: A new array with elements multiplied
    
    Raises:
        ValueError: If input arrays have different lengths
        TypeError: If arrays contain non-numeric elements
    """
    # Check if input arrays have the same length
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) and isinstance(y, (int, float)) for x, y in zip(arr1, arr2)):
        raise TypeError("All array elements must be numeric")
    
    # Multiply corresponding elements
    return [x * y for x, y in zip(arr1, arr2)]