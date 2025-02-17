import unicodedata

def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. This function is case-insensitive
    and ignores whitespace.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    """
    # Normalize Unicode characters and remove accents
    def normalize(s: str) -> str:
        return ''.join(
            char for char in unicodedata.normalize('NFKD', s)
            if not unicodedata.combining(char)
        ).replace(" ", "").lower()
    
    cleaned_str1 = normalize(str1)
    cleaned_str2 = normalize(str2)
    
    # Quick length check
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Convert to sorted character lists and compare
    return sorted(cleaned_str1) == sorted(cleaned_str2)