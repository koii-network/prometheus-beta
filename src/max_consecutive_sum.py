def max_consecutive_substring_sum(s: str) -> int:
    """
    Calculate the maximum sum of consecutive characters that are also consecutive in the input string.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Maximum sum of consecutive characters
    
    Examples:
        >>> max_consecutive_substring_sum("abcabcbb")
        6
        >>> max_consecutive_substring_sum("aabacbaa")
        3
        >>> max_consecutive_substring_sum("")
        0
    """
    if not s:
        return 0
    
    # Track current sum and max sum
    current_sum = 0
    max_sum = 0
    
    # Track consecutive characters
    current_chars = set()
    
    for i in range(len(s)):
        # If current character is not in current set, add it
        if s[i] not in current_chars:
            current_chars.add(s[i])
            current_sum += ord(s[i])
        else:
            # Reset if character is already in set
            current_chars = {s[i]}
            current_sum = ord(s[i])
        
        # Update max sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum