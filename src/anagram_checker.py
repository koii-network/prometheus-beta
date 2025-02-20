def isAnagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
    This function is case-insensitive and ignores whitespace.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    """
    # Normalize the strings by converting to lowercase and removing all whitespace
    normalized1 = ''.join(char for char in str1.lower() if char.isalnum())
    normalized2 = ''.join(char for char in str2.lower() if char.isalnum())
    
    # Check if the sorted character lists are the same
    return sorted(normalized1) == sorted(normalized2)