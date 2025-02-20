def capitalize_strings(input_strings):
    """
    Takes an array of strings and returns a new array with each string capitalized.
    
    Args:
        input_strings (list): A list of strings to be capitalized
    
    Returns:
        list: A new list with each string capitalized
    
    Raises:
        TypeError: If input is not a list
        ValueError: If any element in the list is not a string
    """
    # Validate input is a list
    if not isinstance(input_strings, list):
        raise TypeError("Input must be a list of strings")
    
    # Validate all elements are strings
    if not all(isinstance(item, str) for item in input_strings):
        raise ValueError("All elements must be strings")
    
    # Return a new list with each string capitalized
    return [item.capitalize() for item in input_strings]