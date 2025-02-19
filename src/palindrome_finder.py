def find_non_overlapping_palindromes(s):
    """
    Find all non-overlapping palindromic substrings in the input string.
    
    Args:
        s (str): Input string to find palindromic substrings
    
    Returns:
        list: Sorted list of unique non-overlapping palindromic substrings
    """
    if not s:
        return []
    
    # Helper function to check if a substring is a palindrome
    def is_palindrome(substr):
        return substr == substr[::-1]
    
    palindromes = []
    used_indices = set()
    
    # Iterate through all possible substrings
    for i in range(len(s)):
        # Skip indices already used in previous palindromes
        if i in used_indices:
            continue
        
        for j in range(len(s), i, -1):
            substr = s[i:j]
            
            # Check if substring is a palindrome and uses unused indices
            if (is_palindrome(substr) and 
                all(idx not in used_indices for idx in range(i, j))):
                palindromes.append(substr)
                used_indices.update(range(i, j))
                break
    
    # Return unique palindromes sorted lexicographically
    return sorted(set(palindromes))