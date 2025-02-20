def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Examples:
        >>> is_anagram('listen', 'silent')
        True
        >>> is_anagram('hello', 'world')
        False
    """
    # Remove whitespace and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    
    # Quick check: if lengths are different, they can't be anagrams
    if len(str1) != len(str2):
        return False
    
    # Use sorted comparison
    return sorted(str1) == sorted(str2)