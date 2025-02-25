def find_longest_substring(s: str) -> str:
    """
    Find the longest substring with unique characters.
    
    Args:
        s (str): Input string to search for the longest unique substring
    
    Returns:
        str: The longest substring where each character appears only once
    
    Examples:
        >>> find_longest_substring("abcabcbb")
        'abc'
        >>> find_longest_substring("bbbbb")
        'b'
        >>> find_longest_substring("")
        ''
    """
    if not s:
        return ""
    
    # Sliding window approach
    longest_substring = ""
    start = 0
    char_map = {}
    
    for end, char in enumerate(s):
        # If character is already in the current window, 
        # move the start of the window
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        
        # Update the character's last seen position
        char_map[char] = end
        
        # Update longest substring if current is longer
        current_substring = s[start:end+1]
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    
    return longest_substring