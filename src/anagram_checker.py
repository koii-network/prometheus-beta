def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Examples:
        >>> are_anagrams("listen", "silent")
        True
        >>> are_anagrams("hello", "world")
        False
    """
    # Remove whitespace and convert to lowercase to ensure consistent comparison
    cleaned_str1 = str1.replace(" ", "").lower()
    cleaned_str2 = str2.replace(" ", "").lower()
    
    # Quick length check
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Use character frequency counting
    return sorted(cleaned_str1) == sorted(cleaned_str2)