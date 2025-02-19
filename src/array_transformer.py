def transform_array(arr):
    """
    Transform an array of non-negative integers based on specific rules:
    - 0 remains 0
    - Non-zero elements are transformed to their square plus 1

    Args:
        arr (list): Input list of non-negative integers

    Returns:
        list: Transformed array according to the specified rules
    """
    # Check for non-list input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Validate each element
    for x in arr:
        if not isinstance(x, int):
            raise TypeError("All elements must be integers")
        if x < 0:
            raise TypeError("All elements must be non-negative")
    
    return [0 if x == 0 else x**2 + 1 for x in arr]