def get_unique_sorted_chars(input_string):
    """
    Returns a sorted list of unique characters from the input string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        list: A sorted list of unique characters in case-sensitive alphabetical order.
    
    Examples:
        >>> get_unique_sorted_chars("hello")
        ['e', 'h', 'l', 'o']
        >>> get_unique_sorted_chars("Python")
        ['P', 'h', 'n', 'o', 't', 'y']
        >>> get_unique_sorted_chars("")
        []
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use set to get unique characters, then sort
    unique_chars = sorted(set(input_string))
    
    return unique_chars