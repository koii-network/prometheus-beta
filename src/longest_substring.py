def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.
    
    Args:
        s (str): Input string to search for the longest substring
    
    Returns:
        str: The longest substring without repeating characters
             If multiple such substrings exist, return the first one
    """
    if not s:
        return ""
    
    # Sliding window approach
    start = 0
    max_length = 0
    max_substring = ""
    char_map = {}
    
    for end, char in enumerate(s):
        # If character is already in the current substring, 
        # move the start pointer to the right of the previous occurrence
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        
        # Update the character's last seen position
        char_map[char] = end
        
        # Update max substring if current substring is longer
        current_substring = s[start:end+1]
        if len(current_substring) > max_length:
            max_length = len(current_substring)
            max_substring = current_substring
    
    return max_substring