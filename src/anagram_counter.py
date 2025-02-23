from typing import Set

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
    
    # Set to store unique sorted anagram patterns
    unique_anagrams: Set[str] = set()
    
    # Generate all possible substrings and their sorted anagram patterns
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            # Extract substring and create its sorted representation
            substring = s[i:j]
            sorted_substring = ''.join(sorted(substring))
            unique_anagrams.add(sorted_substring)
    
    return len(unique_anagrams)