def find_longest_substring(s):
    """
    Find the longest substring with unique characters.
    
    Args:
        s (str): Input string to search for longest unique substring
    
    Returns:
        str: Longest substring where each character appears only once
    """
    if not s:
        return ""
    
    longest_substring = ""
    
    for start in range(len(s)):
        # Track unique characters in current substring
        seen = set()
        current_substring = ""
        
        for char in s[start:]:
            # If character is unique in current substring, add it
            if char not in seen:
                seen.add(char)
                current_substring += char
            else:
                # Stop if duplicate found
                break
        
        # Update longest substring if current is longer
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    
    return longest_substring