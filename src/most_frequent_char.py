def find_most_frequent_char(input_string: str) -> str:
    """
    Find the most frequently occurring character in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        str: The most frequently occurring character. 
             If multiple characters have the same highest frequency, 
             returns the first such character encountered.
             Returns an empty string for empty input.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> find_most_frequent_char("hello")
        'l'
        >>> find_most_frequent_char("aabbcc")
        'a'
        >>> find_most_frequent_char("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ''
    
    # Count character frequencies
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find the most frequent character
    return max(char_counts, key=char_counts.get)