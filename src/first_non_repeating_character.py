def first_non_repeating_character(s: str) -> str:
    """
    Find the first non-repeating character in a string.
    
    Args:
        s (str): Input string containing only lowercase letters.
    
    Returns:
        str or None: First non-repeating character, or None if no such character exists.
    """
    # Count the occurrences of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first character with count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If no non-repeating character found
    return None