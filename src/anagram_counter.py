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
    
    # Initialize set to track unique anagram groups
    unique_anagram_groups = set()
    
    # Generate all possible substrings
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            # Sort the substring to identify unique anagram groups
            sorted_substr = ''.join(sorted(s[i:j]))
            unique_anagram_groups.add(sorted_substr)
    
    return len(unique_anagram_groups)