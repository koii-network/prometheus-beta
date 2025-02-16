def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
    
    Returns:
        bool: True if the strings are anagrams, False otherwise.
    
    Notes:
        - The function is case-insensitive.
        - Whitespace is ignored.
        - Spaces and non-alphanumeric characters are removed before comparison.
    """
    # Remove whitespace and convert to lowercase
    cleaned_str1 = ''.join(char.lower() for char in str1 if char.isalnum())
    cleaned_str2 = ''.join(char.lower() for char in str2 if char.isalnum())
    
    # Check if the sorted character lists are equal
    return sorted(cleaned_str1) == sorted(cleaned_str2)