def count_words(input_string: str, separator: str = ' ') -> int:
    """
    Split a given string into words based on a specific separator and return the word count.

    Args:
        input_string (str): The string to be split into words.
        separator (str, optional): The delimiter used to split the string. Defaults to space.

    Returns:
        int: The number of words in the string.

    Raises:
        TypeError: If input_string is not a string or separator is not a string.
        ValueError: If separator is an empty string.

    Examples:
        >>> count_words("hello world")  # Default space separator
        2
        >>> count_words("apple,banana,cherry", separator=",")
        3
        >>> count_words("")  # Empty string
        0
    """
    # Validate input types
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not isinstance(separator, str):
        raise TypeError("Separator must be a string")
    
    # Check for empty separator
    if not separator:
        raise ValueError("Separator cannot be an empty string")
    
    # Handle empty input string
    if not input_string.strip():
        return 0
    
    # Split the string with whitespace stripped, handling multiple whitespaces
    if separator == ' ':
        return len(input_string.strip().split())
    
    # Regular splitting for non-space separators
    return len(input_string.split(separator))