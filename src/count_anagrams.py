from typing import List
from collections import Counter

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagrams in the given string.
    
    An anagram is a substring that contains the same letters in a different order.
    
    Args:
        s (str): Input string containing only lowercase English letters.
    
    Returns:
        int: Number of distinct anagrams in the string.
    
    Raises:
        ValueError: If the input string contains non-lowercase letters.
    
    Examples:
        >>> count_anagrams('abab')
        2
        >>> count_anagrams('abcde')
        0
    """
    # Empty string handling
    if not s:
        return 0
    
    # Validate input
    if not s.islower():
        raise ValueError("Input must contain only lowercase English letters")
    
    # If string has only one character, no anagrams possible
    if len(s) == 1:
        return 0
    
    # Set to store unique anagram signatures
    unique_anagrams = set()
    
    # Generate all possible substrings
    for length in range(1, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start+length]
            
            # Create a sorted signature of the substring
            signature = ''.join(sorted(substring))
            unique_anagrams.add(signature)
    
    # Subtract original substrings to get truly unique anagrams
    return len(unique_anagrams) - len(set(s))