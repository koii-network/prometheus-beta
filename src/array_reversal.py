def reverse_array(arr):
    """
    Takes an integer array and returns a new array with the elements in reverse order.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with elements in reverse order
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    return arr[::-1]