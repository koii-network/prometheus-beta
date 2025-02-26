def count_unique_characters(input_string: str) -> int:
    """
    Count the number of unique characters in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The number of unique characters in the string.
    
    Notes:
        - The function is case-sensitive
        - Empty strings and whitespace-only strings return 0
    
    Examples:
        >>> count_unique_characters('hello')
        4
        >>> count_unique_characters('HELLO')
        5
        >>> count_unique_characters('')
        0
        >>> count_unique_characters('   ')
        0
    """
    # Handle None
    if input_string is None:
        return 0
    
    # Trim whitespace and check if empty after trimming
    input_string = input_string.strip()
    if not input_string:
        return 0
    
    # Use a set to count unique characters
    unique_chars = set(input_string)
    
    return len(unique_chars)