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
    
    # Store unique sorted anagram signatures
    anagram_signatures = set()
    
    # Check all possible substrings
    for length in range(1, len(s) + 1):
        for start in range(len(s) - length + 1):
            # Extract substring and create sorted signature 
            substring = s[start:start+length]
            signature = ''.join(sorted(substring))
            anagram_signatures.add(signature)
    
    return len(anagram_signatures)