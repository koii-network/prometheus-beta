def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.

    This function is case-sensitive and returns the first longest substring 
    if multiple substrings of the same maximum length exist.

    Args:
        s (str): Input string to search for the longest substring

    Returns:
        str: The longest substring without repeating characters
        
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
    
    # Initialize variables to track the longest substring
    longest = ""
    current = ""
    
    for char in s:
        # If character is not in current substring, add it
        if char not in current:
            current += char
        else:
            # If character is repeated, update longest if needed
            # and reset current substring from the repeated character
            if len(current) > len(longest):
                longest = current
            
            # Slice the current substring from the first occurrence of the repeated char
            current = current[current.index(char) + 1:] + char
    
    # Final check to update longest substring
    if len(current) > len(longest):
        longest = current
    
    return longest