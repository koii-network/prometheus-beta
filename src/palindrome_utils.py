def find_palindromic_substrings(s):
    """
    Find all palindromic substrings in a given string.
    
    Args:
        s (str): Input string to find palindromic substrings.
    
    Returns:
        list: A list of all palindromic substrings, including single characters.
    """
    if not s:
        return []
    
    palindromes = []
    
    # Check for odd-length palindromes
    for center in range(len(s)):
        # Expand around center
        left = right = center
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left:right+1])
            left -= 1
            right += 1
    
    # Check for even-length palindromes
    for center in range(len(s) - 1):
        # Expand around center between two characters
        left = center
        right = center + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left:right+1])
            left -= 1
            right += 1
    
    # Remove duplicates while preserving order
    return list(dict.fromkeys(palindromes))