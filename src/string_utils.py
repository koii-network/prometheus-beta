def capitalize_strings(string_array):
    """
    Capitalizes each string in the given array.

    Args:
        string_array (list): A list of strings to be capitalized.

    Returns:
        list: A new list with each string capitalized.

    Raises:
        TypeError: If the input is not a list.
        TypeError: If any element in the list is not a string.
    """
    # Validate input is a list
    if not isinstance(string_array, list):
        raise TypeError("Input must be a list of strings")
    
    # Validate all elements are strings
    if not all(isinstance(item, str) for item in string_array):
        raise TypeError("All elements must be strings")
    
    # Capitalize each string and return a new list
    return [item.capitalize() for item in string_array]