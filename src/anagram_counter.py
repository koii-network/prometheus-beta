def count_anagrams(s):
    """
    Count the number of distinct anagrams in the given string.
    
    Args:
        s (str): A string containing only lowercase English letters.
    
    Returns:
        int: The number of distinct anagrams in the string.
    
    Raises:
        ValueError: If the input string contains non-lowercase letters.
    """
    # Validate input
    if not s or not s.islower():
        raise ValueError("Input must be a non-empty string with only lowercase letters")
    
    # Use a set to store unique sorted anagram signatures
    anagram_signatures = set()
    
    # Generate all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            # Sort the characters of the substring to create an anagram signature
            substring = s[i:j]
            sorted_substring = ''.join(sorted(substring))
            anagram_signatures.add(sorted_substring)
    
    return len(anagram_signatures)