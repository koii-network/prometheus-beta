def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. The comparison is case-insensitive
    and ignores whitespace.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    """
    # Normalize the strings by converting to lowercase and removing whitespace
    normalized_str1 = str1.lower().replace(' ', '')
    normalized_str2 = str2.lower().replace(' ', '')
    
    # Check if the lengths are different
    if len(normalized_str1) != len(normalized_str2):
        return False
    
    # Use sorted characters to compare
    return sorted(normalized_str1) == sorted(normalized_str2)