def arrayMashup(array1, array2):
    """
    Combine two arrays by summing elements at corresponding indices.

    Args:
        array1 (list): First list of positive integers
        array2 (list): Second list of positive integers

    Returns:
        list: A new list where each element is the sum of elements 
              at corresponding indices from input arrays

    Raises:
        ValueError: If either input is not a list of positive integers
        ValueError: If input arrays have different lengths
    """
    # Validate input types
    if not (isinstance(array1, list) and isinstance(array2, list)):
        raise ValueError("Inputs must be lists")
    
    # Validate that all elements are positive integers
    def validate_positive_integers(arr, arr_name):
        if not all(isinstance(x, int) and x > 0 for x in arr):
            raise ValueError(f"{arr_name} must contain only positive integers")
    
    validate_positive_integers(array1, "array1")
    validate_positive_integers(array2, "array2")
    
    # Check array lengths
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length")
    
    # Perform element-wise sum
    return [a + b for a, b in zip(array1, array2)]