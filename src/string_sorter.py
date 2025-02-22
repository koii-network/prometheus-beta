def sort_strings_by_length(strings, reverse=False):
    """
    Sort a list of strings by their length.
    
    Args:
        strings (list): A list of strings to be sorted
        reverse (bool, optional): If True, sort in descending order. Defaults to False.
    
    Returns:
        list: A new list of strings sorted by length
    """
    if not isinstance(strings, list):
        raise TypeError("Input must be a list")
    
    return sorted(strings, key=len, reverse=reverse)