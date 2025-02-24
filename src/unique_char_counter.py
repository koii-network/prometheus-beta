def count_unique_characters(input_string: str) -> int:
    """
    Count the number of unique characters in a given string.
    
    Characters are case-sensitive, meaning 'a' and 'A' are considered different characters.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The number of unique characters in the string.
    
    Examples:
        >>> count_unique_characters('hello')
        4
        >>> count_unique_characters('aAaA')
        2
        >>> count_unique_characters('AbA')
        3
        >>> count_unique_characters('')
        0
        >>> count_unique_characters('   ')
        1
    """
    # Handle None input
    if input_string is None:
        return 0
    
    # Use a set to count unique characters, preserving case sensitivity
    return len(set(char for char in input_string))