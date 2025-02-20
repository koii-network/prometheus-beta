def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are valid anagrams of each other.
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
    
    Returns:
        bool: True if the strings are anagrams, False otherwise.
    
    Raises:
        ValueError: If the input strings contain non-lowercase letters.
    """
    # Check if inputs are valid (only lowercase letters or empty)
    if not all(s.islower() or s == '' for s in (str1, str2)):
        raise ValueError("Input strings must contain only lowercase letters")
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Compare character counts
    return sorted(str1) == sorted(str2)