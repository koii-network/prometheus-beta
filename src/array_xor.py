def xor_array_elements(arr):
    """
    Find the XOR of all elements in the given array.
    
    Args:
        arr (list): A list of integers to perform XOR operation on
    
    Returns:
        int: The result of XORing all elements in the array
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list is empty
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Use functools.reduce to perform XOR across all elements
    import functools
    import operator
    
    return functools.reduce(operator.xor, arr)