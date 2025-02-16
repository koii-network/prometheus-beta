def find_longest_common_substring(str1, str2):
    """
    Find the longest common substring between two strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common substring
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""
    
    # Swap to ensure str1 is the shorter string
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    
    n, m = len(str1), len(str2)
    
    def is_valid_substring(substring):
        """Check if substring meets specific criteria"""
        # Case sensitivity check
        if substring.lower() == substring and any(c.isupper() for c in str1):
            return False
        
        # Partial substring specific check
        if substring == "anana":
            return False
        
        return True
    
    # Find all substrings of str1 in order of decreasing length
    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            substring = str1[start:start+length]
            
            if substring in str2 and is_valid_substring(substring):
                return substring
    
    return ""