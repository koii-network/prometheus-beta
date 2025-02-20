def count_words_by_separator(input_string: str, separator: str = ' ') -> int:
    """
    Split a given string into words based on a specific separator and return the number of words.
    
    Args:
        input_string (str): The string to be split into words.
        separator (str, optional): The separator to use for splitting. Defaults to space.
    
    Returns:
        int: The number of words in the string.
    
    Raises:
        TypeError: If input_string is not a string or separator is not a string.
        ValueError: If separator is an empty string.
    """
    # Type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not isinstance(separator, str):
        raise TypeError("Separator must be a string")
    
    # Check for empty separator
    if separator == '':
        raise ValueError("Separator cannot be an empty string")
    
    # Handle empty input string
    if not input_string:
        return 0
    
    # Split the string and count words
    words = input_string.split(separator)
    return len([word for word in words if word])  # Filter out empty strings