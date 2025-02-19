def longest_unique_substring(s: str) -> int:
    """
    Find the length of the longest substring where no character is repeated.
    
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
    
    # Dictionary to store the last seen index of each character
    char_index = {}
    
    # Variables to track the maximum substring length and current substring start
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If character is already seen and its last position is after or equal to current start
        if char in char_index and char_index[char] >= start:
            # Move the start to the next position after the last occurrence
            start = char_index[char] + 1
        else:
            # Update max length if current substring is longer
            max_length = max(max_length, end - start + 1)
        
        # Update the last seen index of current character
        char_index[char] = end
    
    return max_length