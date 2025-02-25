def sort_integers(arr):
    """
    Sort an array of integers in non-decreasing order.
    
    Args:
        arr (list): A list of integers to be sorted.
    
    Returns:
        list: A new list with integers sorted in non-decreasing order.
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Return a sorted copy of the input list
    return sorted(arr)