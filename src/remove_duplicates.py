def remove_duplicate_chars(input_string: str) -> str:
    """
    Remove duplicate characters from the input string while preserving order.
    
    Args:
        input_string (str): A string containing only lowercase characters
    
    Returns:
        str: A string with duplicate characters removed, preserving the first occurrence
    
    Raises:
        ValueError: If the input contains non-lowercase characters
    """
    # Validate input contains only lowercase characters
    if not input_string.islower():
        raise ValueError("Input string must contain only lowercase characters")
    
    # Use a set to track seen characters while preserving order
    seen_chars = set()
    result = []
    
    for char in input_string:
        if char not in seen_chars:
            result.append(char)
            seen_chars.add(char)
    
    return ''.join(result)