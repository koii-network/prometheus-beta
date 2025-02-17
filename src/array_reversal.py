def reverse_array(arr):
    """
    Reverses the order of elements in the given array or list.
    
    Args:
        arr (list): The input array/list to be reversed.
    
    Returns:
        list: A new list with elements in reversed order.
    
    Raises:
        TypeError: If the input is not a list or array-like object.
    """
    if not hasattr(arr, '__iter__'):
        raise TypeError("Input must be an iterable (list, tuple, etc.)")
    
    return list(reversed(arr))