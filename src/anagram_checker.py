def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
    Ignores case and whitespace.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    """
    # Remove whitespace and convert to lowercase
    cleaned_str1 = ''.join(str1.lower().split())
    cleaned_str2 = ''.join(str2.lower().split())
    
    # Check if the sorted characters are the same
    return sorted(cleaned_str1) == sorted(cleaned_str2)