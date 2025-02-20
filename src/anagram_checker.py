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
    def normalize(s: str) -> str:
        return ''.join(sorted(char.lower() for char in s if char.isalnum()))
    
    # Compare the normalized strings
    return normalize(str1) == normalize(str2)