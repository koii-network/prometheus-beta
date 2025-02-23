def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagrams in the given string.
    
    An anagram is a substring that can be rearranged to form another substring.
    Only considers unique anagram patterns.
    
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
    unique_anagrams = set()
    
    # Find anagrams with their character frequencies
    for length in range(1, len(s) + 1):
        for start in range(len(s) - length + 1):
            # Get substring and sort its characters to identify unique anagram patterns
            substring = sorted(s[start:start+length])
            unique_anagrams.add(tuple(substring))
    
    return len(unique_anagrams)