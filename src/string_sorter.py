def sort_strings_by_length(strings, reverse=False):
    """
    Sort a list of strings by their length.
    
    Args:
        strings (list): A list of strings to be sorted
        reverse (bool, optional): If True, sort in descending order. Defaults to False.
    
    Returns:
        list: A new list of strings sorted by length
    
    Raises:
        TypeError: If input is not a list or contains non-string elements
    """
    # Validate input
    if not isinstance(strings, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # Sort the list by length
    return sorted(strings, key=len, reverse=reverse)