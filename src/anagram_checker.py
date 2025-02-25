def are_anagrams(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
    The function is case-insensitive and ignores whitespace.

    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Raises:
        TypeError: If either input is not a string
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both arguments must be strings")
    
    # Remove whitespace and convert to lowercase
    cleaned_str1 = ''.join(str1.lower().split())
    cleaned_str2 = ''.join(str2.lower().split())
    
    # Check if the sorted characters are the same
    return sorted(cleaned_str1) == sorted(cleaned_str2)