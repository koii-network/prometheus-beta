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
        >>> longest_unique_substring("")
        0
    """
    if not s:
        return 0
    
    # Use sliding window technique
    char_index = {}  # Dictionary to store last seen index of each character
    start = 0
    max_length = 0
    
    for end, char in enumerate(s):
        # If character is already in window and its last position is after or at start
        if char in char_index and char_index[char] >= start:
            # Move start to the next position after the last occurrence
            start = char_index[char] + 1
        
        # Update max length
        max_length = max(max_length, end - start + 1)
        
        # Update last seen index of current character
        char_index[char] = end
    
    return max_length