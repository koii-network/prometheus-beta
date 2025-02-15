def count_occurrences(arr, element):
    """
    Count the number of times a specific element appears in an array.
    
    Args:
        arr (list): The input array to search
        element: The element to count occurrences of
    
    Returns:
        int: Number of times the element appears in the array
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    return arr.count(element)