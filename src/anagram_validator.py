def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are valid anagrams of each other.
    
    Args:
        str1 (str): First input string (lowercase letters only)
        str2 (str): Second input string (lowercase letters only)
    
    Returns:
        bool: True if strings are anagrams, False otherwise
    
    Raises:
        ValueError: If input strings contain non-lowercase letters
    """
    # Validate input contains only lowercase letters
    if not (str1.islower() and str2.islower()):
        raise ValueError("Input strings must contain only lowercase letters")
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}
    
    # Count character frequencies
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequencies
    return char_count1 == char_count2