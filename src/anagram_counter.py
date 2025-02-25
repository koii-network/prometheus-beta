def count_anagrams(s):
    """
    Count the number of distinct anagrams in a given string.
    
    An anagram is a rearrangement of letters that forms a different word.
    
    Args:
        s (str): Input string containing only lowercase English letters.
    
    Returns:
        int: Number of distinct anagrams in the string.
    
    Raises:
        ValueError: If input is not a string of lowercase English letters.
    """
    # Validate input
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    # Allow empty string
    if len(s) == 0:
        return 0
    
    # Validate input contains only lowercase letters
    if not s.islower() or not s.isalpha():
        raise ValueError("Input must contain only lowercase English letters")
    
    # If string is single character, return 0
    if len(s) == 1:
        return 0
    
    # Set to store unique anagram sorted representations
    unique_anagrams = set()
    
    # Generate all possible substrings that are at least 2 characters long
    for length in range(2, len(s) + 1):
        for start in range(len(s) - length + 1):
            # Sort the substring to identify unique anagram groups
            sorted_substring = ''.join(sorted(s[start:start+length]))
            unique_anagrams.add(sorted_substring)
    
    return len(unique_anagrams)