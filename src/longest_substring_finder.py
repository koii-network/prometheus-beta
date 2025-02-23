def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.
    
    Args:
        s (str): Input string to search for the longest unique substring
    
    Returns:
        str: The longest substring without repeating characters
             If multiple substrings have the same maximum length, 
             return the first occurrence
    
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
    longest_substring = ""
    current_substring = ""
    
    for char in s:
        # If character is not in current substring, add it
        if char not in current_substring:
            current_substring += char
        else:
            # If character is already in substring, 
            # update longest substring if needed and reset current substring
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            
            # Slice the current substring from the first repeated character
            current_substring = current_substring[current_substring.index(char) + 1:] + char
    
    # Final check to update longest substring if needed
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
    
    return longest_substring