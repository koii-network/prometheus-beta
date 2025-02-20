def arrayMashup(array1, array2):
    """
    Combine two arrays by summing elements at corresponding indices.
    
    Args:
        array1 (list): First list of positive integers
        array2 (list): Second list of positive integers
    
    Returns:
        list: A new array where each element is the sum of elements at corresponding indices
    
    Raises:
        ValueError: If the input arrays have different lengths
    """
    # Check if arrays have the same length
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length")
    
    # Create a new array by summing corresponding elements
    return [a + b for a, b in zip(array1, array2)]