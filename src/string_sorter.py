def sort_strings_by_length(strings):
    """
    Sort a list of strings by their length in ascending order.
    
    Args:
        strings (list): A list of strings to be sorted.
    
    Returns:
        list: A new list with strings sorted by length.
    
    Raises:
        TypeError: If the input is not a list.
        TypeError: If the list contains non-string elements.
    """
    # Type checking
    if not isinstance(strings, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # Sort the list by length 
    return sorted(strings, key=len)