def count_unique_characters(input_string: str) -> int:
    """
    Count the number of unique characters in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: Number of unique characters in the string.
    
    Notes:
        - Characters are case-sensitive (e.g., 'a' and 'A' are different)
        - Empty or whitespace-only strings return 0
    """
    # Handle empty or whitespace-only strings
    if not input_string or input_string.isspace():
        return 0
    
    # Use a set to count unique characters (preserves case sensitivity)
    return len(set(input_string))