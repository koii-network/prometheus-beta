def xor_array(arr):
    """
    Compute the XOR of all elements in an array.
    
    Args:
        arr (list): A list of integers to compute XOR on.
    
    Returns:
        int: The result of XORing all elements in the array.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input list is empty.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Compute XOR using reduce with initial value 0
    result = 0
    for num in arr:
        result ^= num
    
    return result