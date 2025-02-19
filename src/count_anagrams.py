from typing import Set
from itertools import permutations

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagrams in the given string.
    
    An anagram is a sequence of characters that can be rearranged to form another 
    meaningful sequence using all the original characters exactly once.
    
    Args:
        s (str): Input string containing only lowercase English letters
    
    Returns:
        int: Number of distinct anagrams in the string
    
    Raises:
        ValueError: If the input contains non-lowercase letters
    """
    # Validate input
    if not s or not all(c.islower() for c in s):
        raise ValueError("Input must be a non-empty string with only lowercase letters")
    
    # Use a set to store unique anagrams
    unique_anagrams: Set[str] = set()
    
    # Generate all possible permutations
    for length in range(1, len(s) + 1):
        for perm in set(''.join(p) for p in permutations(s, length)):
            unique_anagrams.add(perm)
    
    return len(unique_anagrams)