def find_longest_substring(s):
    """
    Find the longest substring where each character is used only once.
    
    Args:
        s (str): Input string to search for the longest unique substring
    
    Returns:
        str: The longest substring with unique characters
    """
    if not s:
        return ""
    
    longest_substring = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract the substring
            substring = s[i:j+1]
            
            # Check if all characters in substring are unique
            if len(set(substring)) == len(substring):
                # Update longest substring if current is longer
                if len(substring) > len(longest_substring):
                    longest_substring = substring
    
    return longest_substring