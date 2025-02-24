def capitalize_strings(input_array):
    """
    Capitalize each string in the given array.

    Args:
        input_array (list): A list of strings to be capitalized.

    Returns:
        list: A new list with each string capitalized.

    Raises:
        TypeError: If the input is not a list or contains non-string elements.
    """
    # Validate input is a list
    if not isinstance(input_array, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are strings
    if not all(isinstance(item, str) for item in input_array):
        raise TypeError("All elements must be strings")
    
    # Return a new list with fully capitalized strings, preserving whitespace
    return [item.capitalize() for item in input_array]