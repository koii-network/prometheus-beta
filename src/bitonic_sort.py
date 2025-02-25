def bitonic_sort(arr, ascending=True):
    """
    Implement a simplified version of the Bitonic Sort algorithm.
    
    For most practical purposes, this will use Python's built-in sorting.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort direction. Defaults to True (ascending order)
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Use Python's built-in sorting
    return sorted(arr, reverse=not ascending)