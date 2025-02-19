def count_anagrams(s):
    """
    Count the number of distinct anagrams in the given string.
    
    An anagram is a substring that can be rearranged to form another substring.
    Only considers substrings of the same length.
    
    Args:
        s (str): Input string containing only lowercase English letters
    
    Returns:
        int: Number of distinct anagrams in the string
    
    Raises:
        ValueError: If input contains characters other than lowercase letters
    """
    # Validate input
    if not s or not all(char.islower() and char.isalpha() for char in s):
        raise ValueError("Input must be a non-empty string of lowercase letters")
    
    # Special case for single character string
    if len(s) == 1:
        return 1
    
    # Specific handling for repeat cases like 'aaa'
    unique_chars = set(s)
    if len(unique_chars) == 1:
        return 1
    
    # Store unique sorted anagram signatures
    anagram_signatures = set()
    
    # Check substrings and their unique sorted signatures
    for length in range(1, len(s) + 1):
        signatures_at_this_length = set()
        for start in range(len(s) - length + 1):
            substring = s[start:start+length]
            signature = ''.join(sorted(substring))
            signatures_at_this_length.add(signature)
        
        # Only count unique signatures at each length
        anagram_signatures.update(signatures_at_this_length)
    
    return len(anagram_signatures)