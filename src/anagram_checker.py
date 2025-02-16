def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once.
    
    Args:
        str1 (str): First string to compare
        str2 (str): Second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Check input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Remove whitespace and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Use character counting method
    return sorted(str1) == sorted(str2)