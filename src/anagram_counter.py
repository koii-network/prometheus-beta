from typing import Set
from collections import Counter

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagrams in the given string.
    
    An anagram is a substring that can be rearranged to form another substring.
    Only considers unique anagram combinations.
    
    Args:
        s (str): Input string containing only lowercase English letters.
    
    Returns:
        int: Number of distinct anagrams in the string.
    
    Raises:
        ValueError: If the input string contains non-lowercase letters.
    
    Examples:
        >>> count_anagrams('abab')
        3
        >>> count_anagrams('aa')
        1
    """
    # Validate input
    if not s or not all(c.islower() for c in s):
        raise ValueError("Input must be a non-empty string with only lowercase letters")
    
    # Set to store unique anagram patterns
    unique_anagrams: Set[str] = set()
    
    # Generate all possible substrings and their sorted anagram patterns
    for i in range(len(s)):
        current_counter = Counter()
        for j in range(i, len(s)):
            # Update current substring's character count
            current_counter[s[j]] += 1
            
            # Convert character counts to a tuple to create hashable anagram pattern
            anagram_pattern = tuple(sorted(current_counter.items()))
            unique_anagrams.add(anagram_pattern)
    
    return len(unique_anagrams)