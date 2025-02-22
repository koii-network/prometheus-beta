def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.
    
    Args:
        s (str): Input string to search for the longest substring
    
    Returns:
        str: The longest substring without repeating characters
    """
    if not s:
        return ""
    
    # Initialize variables
    start = 0
    max_length = 0
    max_substring = ""
    char_map = {}
    
    for end, char in enumerate(s):
        # If character is seen and its last position is after or equal to start
        if char in char_map and char_map[char] >= start:
            # Move start pointer to the next position after last occurrence
            start = char_map[char] + 1
        else:
            # Update max substring if current substring is longer
            current_substring = s[start:end+1]
            if len(current_substring) > len(max_substring):
                max_substring = current_substring
        
        # Update last seen position of current character
        char_map[char] = end
    
    return max_substring