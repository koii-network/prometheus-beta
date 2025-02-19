def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Note:
        - Comparison is case-insensitive
        - Whitespace is ignored
        - Non-alphabetic characters are ignored
    """
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_str1 = ''.join(char.lower() for char in str1 if char.isalpha())
    cleaned_str2 = ''.join(char.lower() for char in str2 if char.isalpha())
    
    # Check if cleaned strings have the same length
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Compare sorted characters
    return sorted(cleaned_str1) == sorted(cleaned_str2)