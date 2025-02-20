def can_convert_by_one_deletion(word1: str, word2: str) -> bool:
    """
    Check if word1 can be converted to word2 by deleting exactly one character.
    
    Args:
        word1 (str): The first word
        word2 (str): The target word
    
    Returns:
        bool: True if word1 can be converted to word2 by deleting one character, False otherwise
    """
    # If lengths differ by more than 1, it's impossible
    if len(word1) != len(word2) + 1:
        return False
    
    # Try removing each character from word1 and check if it matches word2
    for i in range(len(word1)):
        candidate = word1[:i] + word1[i+1:]
        if candidate == word2:
            return True
    
    return False