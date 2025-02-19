def longest_unique_substring(s: str) -> int:
    """
    Find the length of the longest substring with no repeated characters.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Length of the longest substring with unique characters
    
    Examples:
        >>> longest_unique_substring("abcabcbb")
        3
        >>> longest_unique_substring("bbbbb")
        1
        >>> longest_unique_substring("pwwkew")
        3
    """
    if not s:
        return 0
    
    # Use sliding window technique
    char_index = {}  # Dictionary to store last seen index of each character
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If character is seen and its last position is after or at start of current window
        if char in char_index and char_index[char] >= start:
            # Move start to the next position after the last occurrence of repeated char
            start = char_index[char] + 1
        
        # Update max length
        max_length = max(max_length, end - start + 1)
        
        # Update last seen index of current character
        char_index[char] = end
    
    return max_length