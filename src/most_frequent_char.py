def find_most_frequent_char(s: str) -> str:
    """
    Find the most frequently occurring character in a string.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        str: The most frequently occurring character 
             If multiple characters have the same max frequency, 
             return the first one encountered in the string
             If the string is empty, return an empty string
    
    Examples:
        >>> find_most_frequent_char("hello")
        'l'
        >>> find_most_frequent_char("aabbcc")
        'a'
        >>> find_most_frequent_char("")
        ''
    """
    # Handle empty string case
    if not s:
        return ''
    
    # Count character frequencies 
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the character with maximum frequency
    max_freq_char = max(char_count, key=char_count.get)
    
    return max_freq_char