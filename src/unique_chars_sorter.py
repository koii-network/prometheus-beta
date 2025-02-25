def sort_unique_characters(input_string):
    """
    Sort unique characters in a given string in case-sensitive alphabetical order.

    Args:
        input_string (str): The input string to process.

    Returns:
        list: A sorted list of unique characters from the input string.

    Examples:
        >>> sort_unique_characters("hello")
        ['e', 'h', 'l', 'o']
        >>> sort_unique_characters("AaBbCc")
        ['A', 'B', 'C', 'a', 'b', 'c']
        >>> sort_unique_characters("")
        []
    """
    # Handle empty string case
    if not input_string:
        return []
    
    # Convert to list of unique characters and sort using Unicode ordering
    unique_chars = sorted(set(input_string), key=lambda x: str(x))
    
    return unique_chars