def count_unique_characters(input_string):
    """
    Count the number of unique characters in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The number of unique characters in the string.
    
    Notes:
        - Characters are case-sensitive
        - Whitespace and empty strings are handled
    """
    # Handle None input 
    if input_string is None:
        return 0
    
    # Use a set to count unique characters
    unique_chars = set(input_string)
    
    return len(unique_chars)