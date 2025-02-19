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
    
    # Use sliding window technique
    start = 0
    max_length = 0
    max_substring = ""
    char_index = {}
    
    for end, char in enumerate(s):
        # If character is already seen and its last position is after or equal to start
        if char in char_index and char_index[char] >= start:
            # Move start to the next position after last occurrence
            start = char_index[char] + 1
        else:
            # Update max substring if current substring is longer
            if end - start + 1 > max_length:
                max_length = end - start + 1
                max_substring = s[start:end+1]
        
        # Update last seen position of current character
        char_index[char] = end
    
    return max_substring