def find_palindromic_substrings(s: str) -> list:
    """
    Find all palindromic substrings in a given string.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        list: A list of all palindromic substrings found in the input string
    """
    if not s:
        return []
    
    palindromes = []
    
    # Check all possible substrings
    for i in range(len(s)):
        # Odd length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left:right+1])
            left -= 1
            right += 1
        
        # Even length palindromes
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left:right+1])
            left -= 1
            right += 1
    
    # Remove duplicates while preserving order
    return list(dict.fromkeys(palindromes))