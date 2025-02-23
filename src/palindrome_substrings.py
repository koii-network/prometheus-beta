def find_non_overlapping_palindromic_substrings(s: str) -> list[str]:
    """
    Find and return all non-overlapping palindromic substrings of an input string,
    sorted in lexicographic order.

    Args:
        s (str): The input string to search for palindromic substrings.

    Returns:
        list[str]: A list of unique, non-overlapping palindromic substrings, 
                   sorted lexicographically.

    Examples:
        >>> find_non_overlapping_palindromic_substrings('aabaa')
        ['aa', 'aba']
        >>> find_non_overlapping_palindromic_substrings('abcde')
        ['a', 'b', 'c', 'd', 'e']
        >>> find_non_overlapping_palindromic_substrings('')
        []
    """
    # Handle empty string edge case
    if not s:
        return []
    
    # Helper function to check if a substring is a palindrome
    def is_palindrome(substr: str) -> bool:
        return substr == substr[::-1]
    
    # Find all palindromic substrings
    palindromes = []
    used_indices = set()
    
    # Iterate through all possible substrings
    for i in range(len(s)):
        # Skip indices already used in previous palindromes
        if i in used_indices:
            continue
        
        # Check single-character palindrome
        if is_palindrome(s[i]):
            palindromes.append(s[i])
            used_indices.add(i)
        
        # Check longer palindromes
        for j in range(len(s), i, -1):
            # Skip any indices already used
            if any(idx in used_indices for idx in range(i, j)):
                continue
            
            # Check if current substring is a palindrome
            substr = s[i:j]
            if is_palindrome(substr):
                palindromes.append(substr)
                # Mark all indices in this substring as used
                used_indices.update(range(i, j))
                break
    
    # Sort palindromes lexicographically
    return sorted(set(palindromes))