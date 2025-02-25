def count_element_occurrences(arr, element):
    """
    Count the number of times a specific element appears in an array.
    
    Args:
        arr (list): The input array to search
        element: The element to count occurrences of
    
    Returns:
        int: Number of times the element appears in the array
    """
    if arr is None:
        return 0
    
    return arr.count(element)