from typing import Set

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagrams in the given string.
    
    Args:
        s (str): Input string containing only lowercase English letters.
    
    Returns:
        int: Number of distinct anagrams in the string.
    
    Raises:
        ValueError: If the input string contains characters other than lowercase letters.
    """
    # Validate input
    if not s or not all(c.islower() and c.isalpha() for c in s):
        raise ValueError("Input must be a non-empty string of lowercase English letters")
    
    # Use a set to store unique sorted representations of substrings
    anagram_set: Set[str] = set()
    
    # Generate all possible substrings
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            # Sort the characters of the substring to identify anagrams
            sorted_substring = ''.join(sorted(s[start:end]))
            anagram_set.add(sorted_substring)
    
    # Return the number of unique anagram signatures
    return len(anagram_set)