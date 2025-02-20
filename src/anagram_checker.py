def anagram_checker(word1: str, word2: str) -> bool:
    """
    Check if two words are anagrams of each other.
    
    Args:
        word1 (str): First word to compare
        word2 (str): Second word to compare
    
    Returns:
        bool: True if words are anagrams, False otherwise
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Check input types
    if not (isinstance(word1, str) and isinstance(word2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Convert to lowercase and remove any whitespace
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    
    # Check if lengths are different
    if len(word1) != len(word2):
        return False
    
    # Use sorted character comparison
    return sorted(word1) == sorted(word2)