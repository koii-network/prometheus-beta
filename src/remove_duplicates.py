def remove_duplicate_chars(input_string):
    """
    Remove duplicate characters from a given string while preserving the original order.
    Preserves original case and treats each character as potentially unique.
    
    Args:
        input_string (str): The input string to remove duplicates from.
    
    Returns:
        str: A string with duplicate characters removed, keeping the first occurrence.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a list to track seen characters while preserving order
    seen_chars = []
    result = []
    
    for char in input_string:
        # Check if the exact character (including case and spaces) has been seen before
        if char not in seen_chars:
            seen_chars.append(char)
            result.append(char)
    
    return ''.join(result)