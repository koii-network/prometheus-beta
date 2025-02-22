def reverse_array(arr):
    """
    Reverses the order of elements in the given array.
    
    Args:
        arr (list): The input array to be reversed.
    
    Returns:
        list: A new array with elements in reversed order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    return arr[::-1]