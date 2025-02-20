def can_convert_by_one_deletion(word1: str, word2: str) -> bool:
    """
    Check if word1 can be converted to word2 by deleting exactly one character.
    
    Args:
        word1 (str): The first input string
        word2 (str): The target string to convert to
    
    Returns:
        bool: True if word1 can be converted to word2 by deleting exactly one character, 
              False otherwise
    """
    # If the length difference is not exactly 1, return False
    if len(word1) != len(word2) + 1:
        return False
    
    # Try removing each character from word1 and compare with word2
    for i in range(len(word1)):
        # Create a new string by removing the character at index i
        candidate = word1[:i] + word1[i+1:]
        
        # If the resulting string matches word2, return True
        if candidate == word2:
            return True
    
    return False