def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "world")
        False
    """
    # Remove whitespace and convert to lowercase for case-insensitive comparison
    cleaned_str1 = str1.replace(" ", "").lower()
    cleaned_str2 = str2.replace(" ", "").lower()
    
    # Quick length check
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Use character frequency counting
    return sorted(cleaned_str1) == sorted(cleaned_str2)