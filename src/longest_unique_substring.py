def longest_unique_substring_length(s: str) -> int:
    """
    Find the length of the longest substring with no repeated characters.
    
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
        >>> longest_unique_substring_length("")
        0
    """
    # Handle empty string case
    if not s:
        return 0
    
    # Use sliding window technique
    char_index = {}  # Store the last seen index of each character
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If character is already in the current window, 
        # move the start of the window
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            # Update max length if current window is longer
            max_length = max(max_length, end - start + 1)
        
        # Update last seen index of current character
        char_index[char] = end
    
    return max_length