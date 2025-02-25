def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.
    
    Args:
        s (str): Input string to search for the longest unique substring
    
    Returns:
        str: The longest substring without repeating characters
             If multiple substrings have the same max length, 
             return the first occurrence from left to right
    
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
    
    # Use sliding window technique
    char_index = {}
    start = 0
    longest_start = 0
    longest_length = 0
    
    for end, char in enumerate(s):
        # If character is already in the current window, 
        # move the start pointer to the right of its previous occurrence
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        # Update the last seen index of the character
        char_index[char] = end
        
        # Update longest substring if current is longer
        current_length = end - start + 1
        if current_length > longest_length:
            longest_start = start
            longest_length = current_length
    
    return s[longest_start:longest_start + longest_length]