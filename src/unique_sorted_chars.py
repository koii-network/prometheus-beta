def get_unique_sorted_chars(input_string: str) -> list:
    """
    Returns a sorted list of unique characters from the input string.
    
    Args:
        input_string (str): The input string to extract unique characters from.
    
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
    # Use set to get unique characters, then sort in case-sensitive order
    return sorted(set(input_string))