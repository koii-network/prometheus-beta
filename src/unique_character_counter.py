def count_unique_characters(input_string: str) -> int:
    """
    Count the number of unique characters in a given string.
    
    Characters are case-sensitive, meaning 'a' and 'A' are considered different.
    
    Args:
        input_string (str): The input string to analyze
    
    Returns:
        int: Number of unique characters in the string
    
    Examples:
        >>> count_unique_characters("hello")
        4
        >>> count_unique_characters("aAaA")
        2
        >>> count_unique_characters("")
        0
        >>> count_unique_characters("   ")
        1
    """
    # Handle empty string or whitespace-only string
    if not input_string:
        return 0
    
    # Use set to count unique characters, preserving case sensitivity
    return len(set(input_string))