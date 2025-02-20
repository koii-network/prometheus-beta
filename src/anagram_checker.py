def anagram_checker(word1: str, word2: str) -> bool:
    """
    Check if two words are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of a different 
    word or phrase, using all the original letters exactly once.
    
    Args:
        word1 (str): The first word to compare
        word2 (str): The second word to compare
    
    Returns:
        bool: True if the words are anagrams, False otherwise
    
    Examples:
        >>> anagram_checker('listen', 'silent')
        True
        >>> anagram_checker('hello', 'world')
        False
    """
    # Convert to lowercase and remove any whitespace
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')
    
    # Check if lengths are different
    if len(word1) != len(word2):
        return False
    
    # Count character frequencies
    char_count = {}
    
    # Count characters in first word
    for char in word1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract characters from second word
    for char in word2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True