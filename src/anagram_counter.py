from typing import Set

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagrams in the given string.
    
    Args:
        s (str): Input string containing only lowercase English letters
    
    Returns:
        int: Number of distinct anagrams found in the string
    
    Raises:
        ValueError: If the input string contains non-lowercase letters
    """
    # Validate input
    if not s.islower():
        raise ValueError("Input must contain only lowercase English letters")
    
    # If string is empty or single character, return 0
    if len(s) <= 1:
        return 0
    
    # Set to store unique anagrams
    unique_anagrams: Set[str] = set()
    
    # Generate all possible substrings
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            # Extract substring and sort its characters
            substring = s[start:end]
            sorted_substring = ''.join(sorted(substring))
            
            # Add sorted substring to unique anagrams
            unique_anagrams.add(sorted_substring)
    
    return len(unique_anagrams)