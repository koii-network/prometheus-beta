def find_longest_substring(s):
    """
    Find the longest substring without repeating characters.
    
    Args:
        s (str): Input string to search for the longest substring.
    
    Returns:
        str: The longest substring without repeating characters.
    """
    if not s:
        return ""
    
    # Dictionary to store the last seen index of each character
    char_index = {}
    
    # Variables to track the longest substring
    max_length = 0
    start = 0
    longest_start = 0
    
    for end, char in enumerate(s):
        # If character is seen and its last occurrence is after or at the current substring start
        if char in char_index and char_index[char] >= start:
            # Move the start to the next index after the last occurrence
            start = char_index[char] + 1
        else:
            # Update max length if current substring is longer
            if end - start + 1 > max_length:
                max_length = end - start + 1
                longest_start = start
        
        # Update the last seen index of the current character
        char_index[char] = end
    
    # Return the longest substring
    return s[longest_start:longest_start + max_length]