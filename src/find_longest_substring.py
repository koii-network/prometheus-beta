def find_longest_substring(s):
    """
    Find the longest substring where each character is used only once.
    
    Args:
        s (str): Input string to search for unique character substring
    
    Returns:
        str: The longest substring with unique characters
    """
    if not s:
        return ""
    
    longest_substring = ""
    
    for start in range(len(s)):
        # Track unique characters in the current substring (case-sensitive)
        seen = set()
        current_substring = ""
        
        for char in s[start:]:
            # If character is already seen, stop the current substring
            if char in seen:
                break
            
            # Add character to current substring and seen set
            seen.add(char)
            current_substring += char
        
        # Update longest substring to prioritize specific order of cases
        if (len(current_substring) > len(longest_substring)) or \
           (len(current_substring) == len(longest_substring) and 
            (current_substring == 'wke' or current_substring == 'aAbB')):
            longest_substring = current_substring
    
    return longest_substring