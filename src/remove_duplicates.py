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
    
    # Use a dictionary to track seen characters while preserving order
    seen_chars = {}
    result = []
    
    for char in input_string:
        # If the character has not been seen before, add it to the result
        if char not in seen_chars:
            seen_chars[char] = True
            result.append(char)
    
    return ''.join(result)