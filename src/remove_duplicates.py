def remove_duplicate_chars(input_string):
    """
    Remove duplicate characters from the input string while preserving the order 
    of first occurrence of each character.
    
    Args:
        input_string (str): A lowercase string to remove duplicates from.
    
    Returns:
        str: A string with duplicate characters removed.
    
    Raises:
        ValueError: If the input contains non-lowercase characters.
    """
    # Empty string is a valid input
    if not input_string:
        return input_string
    
    # Validate input is lowercase
    if not input_string.islower():
        raise ValueError("Input string must contain only lowercase characters")
    
    # Use a dictionary to preserve order and track unique characters
    seen_chars = {}
    for char in input_string:
        seen_chars[char] = True
    
    # Reconstruct the string with unique characters
    return ''.join(seen_chars.keys())