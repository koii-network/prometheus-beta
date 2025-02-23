def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.

    This function is case-sensitive and returns the first longest substring 
    if multiple substrings of the same maximum length exist.

    Args:
        s (str): Input string to search for the longest substring

    Returns:
        str: The longest substring without repeating characters
        
    Examples:
        >>> find_longest_substring("abcabcbb")
        'abc'
        >>> find_longest_substring("bbbbb")
        'b'
        >>> find_longest_substring("")
        ''
    """
    # Handle empty string case
    if not s:
        return ""
    
    # Initialize variables to track the longest substring
    longest = ""
    start = 0
    char_map = {}
    
    for end, char in enumerate(s):
        # If character is seen before and its last position is after start
        if char in char_map and char_map[char] >= start:
            # Move start to the next position after the last occurrence
            start = char_map[char] + 1
        else:
            # Update longest substring if current is longer
            if end - start + 1 > len(longest):
                longest = s[start:end+1]
        
        # Update last seen position of current character
        char_map[char] = end
    
    return longest