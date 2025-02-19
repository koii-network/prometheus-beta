def find_longest_substring(s):
    """
    Find the longest substring with unique characters.
    
    Args:
        s (str): Input string to search for the longest unique substring
    
    Returns:
        str: The longest substring where each character appears only once
    """
    if not s:
        return ""
    
    # Track the start of the current unique substring
    start = 0
    # Track the longest substring found
    longest_substring = ""
    # Track the last seen position of each character
    char_map = {}
    
    for end in range(len(s)):
        # If character is already seen and its last position is after or equal to start
        if s[end] in char_map and char_map[s[end]] >= start:
            # Move start to the next position after the last occurrence of this character
            start = char_map[s[end]] + 1
        
        # Update the last seen position of current character
        char_map[s[end]] = end
        
        # Check if current substring is longer than the longest found so far
        current_substring = s[start:end+1]
        if len(current_substring) > len(longest_substring) and len(set(current_substring)) == len(current_substring):
            longest_substring = current_substring
    
    return longest_substring