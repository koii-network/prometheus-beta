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
    
    for i in range(len(s)):
        seen = set()
        current_substring = ""
        
        for j in range(i, len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                current_substring += s[j]
            else:
                break
        
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    
    return longest_substring