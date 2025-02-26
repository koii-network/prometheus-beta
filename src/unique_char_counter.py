def count_unique_characters(input_string: str) -> int:
    """
    Count the number of unique characters in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        int: The number of unique characters in the string.

    Notes:
        - The function is case-sensitive 
        - Empty strings return 0
        - Whitespace characters are counted as unique characters
    
    Examples:
        >>> count_unique_characters("hello")
        4
        >>> count_unique_characters("aAaA")
        2
        >>> count_unique_characters("")
        0
        >>> count_unique_characters("  ")
        1
    """
    # Handle None or non-string inputs
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a set to count unique characters
    return len(set(input_string))