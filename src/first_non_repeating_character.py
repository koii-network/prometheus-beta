def first_non_repeating_character(s: str) -> str | None:
    """
    Find the first non-repeating character in a string.

    Args:
        s (str): Input string containing only lowercase letters.

    Returns:
        str | None: The first non-repeating character, or None if no such character exists.

    Raises:
        ValueError: If the input string contains non-lowercase letters.

    Examples:
        >>> first_non_repeating_character("leetcode")
        'l'
        >>> first_non_repeating_character("loveleetcode")
        'v'
        >>> first_non_repeating_character("aabb")
        None
    """
    # Validate input 
    if not s or not s.islower():
        raise ValueError("Input must be a non-empty string of lowercase letters")
    
    # Count occurrences of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first character with count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If no non-repeating character found
    return None