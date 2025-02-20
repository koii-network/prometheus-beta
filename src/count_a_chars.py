def count_a_chars(input_string):
    """
    Count the number of times the character 'a' appears in the given string, 
    ignoring case sensitivity.
    
    Args:
        input_string (str): The string to search for 'a' characters.
    
    Returns:
        int: The number of times 'a' appears in the string (case-insensitive).
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.lower().count('a')