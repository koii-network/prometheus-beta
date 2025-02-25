def remove_excess_duplicates(input_string):
    """
    Remove duplicate characters that appear more than twice in a given string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A modified string with duplicates appearing more than twice removed.
    
    Examples:
        >>> remove_excess_duplicates("aabbcccd")
        'aabbcd'
        >>> remove_excess_duplicates("hello")
        'helo'
        >>> remove_excess_duplicates("aaaaabbbcccccd")
        'aabbbcd'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Count character frequencies
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Build result string, keeping characters that appear 1-2 times
    result = []
    for char in input_string:
        if char_count[char] <= 2 or result.count(char) < 2:
            result.append(char)
    
    return ''.join(result)