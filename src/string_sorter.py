def sort_strings_by_length(strings):
    """
    Sort a list of strings by their length in ascending order.
    
    Args:
        strings (list): A list of strings to be sorted.
    
    Returns:
        list: A new list of strings sorted by length in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-string elements.
    """
    # Check if input is a list
    if not isinstance(strings, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements in the list must be strings")
    
    # Sort the list based on length
    return sorted(strings, key=len)