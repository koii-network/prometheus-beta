def reverse_array(arr):
    """
    Reverse the order of elements in an array.
    
    Args:
        arr (list): The input array to be reversed.
    
    Returns:
        list: A new array with elements in reversed order.
    
    Raises:
        TypeError: If input is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    return arr[::-1]