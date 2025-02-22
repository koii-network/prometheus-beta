def remove_duplicate_chars(input_string):
    """
    Remove duplicate characters from a given string while preserving the original order.
    
    Args:
        input_string (str): The input string from which duplicates should be removed.
    
    Returns:
        str: A string with duplicate characters removed, keeping the first occurrence of each character.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    seen_chars = set()
    result = []
    
    for char in input_string:
        if char not in seen_chars:
            result.append(char)
            seen_chars.add(char)
    
    return ''.join(result)