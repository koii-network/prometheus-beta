def count_occurrences(arr, element):
    """
    Count the number of times a specific element appears in an array.
    
    Args:
        arr (list): The input array to search through
        element: The element to count occurrences of
    
    Returns:
        int: The number of times the element appears in the array
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    return arr.count(element)