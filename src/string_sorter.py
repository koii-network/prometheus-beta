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
    # Validate input is a list
    if not isinstance(strings, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # Return a new list sorted by length, with stable sorting
    return sorted(strings, key=lambda x: (len(x), x))