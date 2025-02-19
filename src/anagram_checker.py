def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Notes:
    - Comparison is case-insensitive
    - Ignores whitespace
    - Returns False if inputs are not strings
    """
    # Check if inputs are strings
    if not (isinstance(str1, str) and isinstance(str2, str)):
        return False
    
    # Remove whitespace and convert to lowercase
    cleaned_str1 = ''.join(str1.lower().split())
    cleaned_str2 = ''.join(str2.lower().split())
    
    # Check if lengths are different
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Compare character frequencies
    return sorted(cleaned_str1) == sorted(cleaned_str2)