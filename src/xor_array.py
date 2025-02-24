def xor_array_elements(arr):
    """
    Calculate the XOR of all elements in the given array.

    Args:
        arr (list): A list of integers to perform XOR operation on.

    Returns:
        int: The result of XOR-ing all elements in the array.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input list is empty.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Perform XOR reduction
    result = arr[0]
    for x in arr[1:]:
        result ^= x
    
    return result