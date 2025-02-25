def xor_array_elements(arr):
    """
    Calculate the XOR of all elements in the given array.
    
    Args:
        arr (list): A list of integers to perform XOR operation on.
    
    Returns:
        int: The result of XOR-ing all elements in the array.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Perform XOR of all elements
    result = arr[0]
    for num in arr[1:]:
        result ^= num
    
    return result