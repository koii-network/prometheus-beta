def reverse_integer_array(arr):
    """
    Takes an integer array and returns a new array with elements in reverse order.
    
    Args:
        arr (list): An input list of integers
    
    Returns:
        list: A new list with elements in reverse order
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    return arr[::-1]