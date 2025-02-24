def reverse_integer_array(arr):
    """
    Reverse the order of elements in an integer array.

    Args:
        arr (list): An input list of integers to be reversed.

    Returns:
        list: A new list with elements in reverse order.

    Raises:
        TypeError: If the input is not a list.
        TypeError: If any element in the list is not an integer.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Return a new list with elements reversed
    return arr[::-1]