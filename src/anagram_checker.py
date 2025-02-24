def isAnagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. The comparison is case-insensitive and 
    ignores whitespace.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        TypeError: If either input is not a string
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Remove whitespace and convert to lowercase
    cleaned_str1 = str1.replace(" ", "").lower()
    cleaned_str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths are different
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}
    
    # Count character frequencies
    for char in cleaned_str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in cleaned_str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequency dictionaries
    return char_count1 == char_count2