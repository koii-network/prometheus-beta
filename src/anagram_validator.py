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
    # Check if inputs are valid (only lowercase letters)
    if not (str1.islower() and str2.islower()):
        raise ValueError("Input strings must contain only lowercase letters")
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Compare character counts
    return sorted(str1) == sorted(str2)