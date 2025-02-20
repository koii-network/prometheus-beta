def multiply_array_elements(arr1, arr2):
    """
    Multiply corresponding elements from two input arrays.
    
    Args:
        arr1 (list): First input array 
        arr2 (list): Second input array
    
    Returns:
        list: A new list with elements multiplied pairwise
    
    Raises:
        ValueError: If the input arrays have different lengths
    """
    # Check if arrays have the same length
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length")
    
    # Multiply corresponding elements 
    return [a * b for a, b in zip(arr1, arr2)]