def find_palindromic_substrings(s):
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
    
    # Helper function to expand around center
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.append(s[left:right+1])
            left -= 1
            right += 1
    
    # Check for odd and even length palindromes
    for i in range(len(s)):
        # Odd length palindromes
        expand_around_center(i, i)
        
        # Even length palindromes
        expand_around_center(i, i+1)
    
    # Return unique palindromes in the order of discovery
    return list(dict.fromkeys(palindromes))