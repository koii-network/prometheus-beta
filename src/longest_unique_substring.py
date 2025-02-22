def longest_unique_substring_length(s: str) -> int:
    """
    Find the length of the longest substring where no character is repeated.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Length of the longest substring with unique characters
    
    Examples:
        >>> longest_unique_substring_length("abcabcbb")
        3
        >>> longest_unique_substring_length("bbbbb")
        1
        >>> longest_unique_substring_length("pwwkew")
        3
    """
    if not s:
        return 0
    
    # Use sliding window technique
    char_index = {}  # Dictionary to store last seen index of each character
    start = 0  # Start of the current window
    max_length = 0  # Maximum length of unique substring
    
    for end, char in enumerate(s):
        # If character is already in the window, move start to the right
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        # Update last seen index of current character
        char_index[char] = end
        
        # Update max length
        max_length = max(max_length, end - start + 1)
    
    return max_length