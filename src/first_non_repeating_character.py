def first_non_repeating_character(s: str) -> str:
    """
    Find the first non-repeating character in a lowercase string.
    
    Args:
        s (str): Input string containing only lowercase letters
    
    Returns:
        str or None: First non-repeating character or None if no such character exists
    """
    # Create a dictionary to count character frequencies
    char_count = {}
    
    # First pass: Count character frequencies
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Second pass: Find first character with count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If no non-repeating character found
    return None