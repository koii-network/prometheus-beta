def remove_duplicate_chars(input_string):
    """
    Remove duplicate characters from a given string while preserving the original order.
    
    Args:
        input_string (str): The input string to remove duplicates from.
    
    Returns:
        str: A string with duplicate characters removed, keeping the first occurrence.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a set to track seen characters while preserving order
    seen_chars = set()
    result = []
    
    for char in input_string:
        if char not in seen_chars:
            result.append(char)
            seen_chars.add(char)
    
    return ''.join(result)