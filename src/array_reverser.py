def reverse_array(arr):
    """
    Reverse the order of elements in an array/list.
    
    Args:
        arr (list): The input list to be reversed.
    
    Returns:
        list: A new list with elements in reverse order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    return arr[::-1]