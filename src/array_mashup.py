def arrayMashup(array1, array2):
    """
    Combine two arrays by summing elements at corresponding indices.

    Args:
        array1 (list): First input array of positive integers
        array2 (list): Second input array of positive integers

    Returns:
        list: A new array where each element is the sum of elements 
              at corresponding indices from input arrays

    Raises:
        ValueError: If input arrays are empty
        TypeError: If inputs are not lists of positive integers
    """
    # Validate input types
    if not (isinstance(array1, list) and isinstance(array2, list)):
        raise TypeError("Inputs must be lists")
    
    # Check for empty arrays
    if len(array1) == 0 or len(array2) == 0:
        raise ValueError("Input arrays cannot be empty")
    
    # Check that all elements are positive integers
    if not (all(isinstance(x, int) and x > 0 for x in array1) and 
            all(isinstance(x, int) and x > 0 for x in array2)):
        raise TypeError("All elements must be positive integers")
    
    # Check if arrays have different lengths
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length")
    
    # Compute the mashup
    return [a + b for a, b in zip(array1, array2)]