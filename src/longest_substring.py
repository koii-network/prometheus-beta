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
    
    # Initialize variables to track the longest substring
    longest = ""
    current = ""
    
    for char in s:
        # If char is already in current substring, 
        # trim the substring from the first occurrence of the repeated char
        if char in current:
            # Find the index of the first occurrence and slice
            current = current[current.index(char) + 1:] + char
        else:
            # Append the new character
            current += char
        
        # Update longest substring if current is longer
        if len(current) > len(longest):
            longest = current
    
    return longest