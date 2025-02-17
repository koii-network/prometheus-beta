def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. The comparison is case-insensitive and 
    ignores whitespace.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both arguments must be strings")
    
    # Remove whitespace and convert to lowercase
    cleaned_str1 = str1.replace(" ", "").lower()
    cleaned_str2 = str2.replace(" ", "").lower()
    
    # Quick length check to avoid unnecessary sorting
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Sort the characters and compare
    return sorted(cleaned_str1) == sorted(cleaned_str2)