def arrayMashup(array1, array2):
    """
    Combine two arrays by summing elements at corresponding indices.
    
    Args:
        array1 (list): First list of positive integers
        array2 (list): Second list of positive integers
    
    Returns:
        list: A new list where each element is the sum of elements 
              at corresponding indices of input arrays
    
    Raises:
        ValueError: If arrays have different lengths
        TypeError: If arrays contain non-integer elements
    """
    # Validate input arrays have the same length
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length")
    
    # Validate all elements are positive integers
    if not all(isinstance(x, int) and x > 0 for x in array1 + array2):
        raise TypeError("All elements must be positive integers")
    
    # Create new array by summing corresponding elements
    return [a + b for a, b in zip(array1, array2)]