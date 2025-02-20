def capitalize_strings(string_array):
    """
    Takes an array of strings and returns a new array with each string capitalized.
    
    Args:
        string_array (list): A list of strings to be capitalized.
    
    Returns:
        list: A new list with each string capitalized.
    
    Raises:
        TypeError: If the input is not a list or contains non-string elements.
    """
    if not isinstance(string_array, list):
        raise TypeError("Input must be a list of strings")
    
    try:
        return [s.capitalize() for s in string_array]
    except AttributeError:
        raise TypeError("All elements in the list must be strings")