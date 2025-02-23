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
    
    # Helper function to check palindrome
    def is_palindrome(substring: str) -> bool:
        return substring == substring[::-1]
    
    # Generate all palindromic substrings
    def get_palindromes(s: str) -> list[str]:
        palindromes = []
        n = len(s)
        
        # Single character palindromes
        for i in range(n):
            if is_palindrome(s[i]):
                palindromes.append(s[i])
        
        # Longer palindromes
        for length in range(2, n+1):
            for start in range(n - length + 1):
                substr = s[start:start+length]
                if is_palindrome(substr):
                    palindromes.append(substr)
        
        return sorted(set(palindromes), key=lambda x: (len(x), x))
    
    # Get all palindromes
    all_palindromes = get_palindromes(s)
    
    # Non-overlapping selection
    result = []
    used_indices = set()
    
    for palindrome in all_palindromes:
        # Find all occurrences
        for i in range(len(s)):
            # Check if current substring matches palindrome
            if s[i:i+len(palindrome)] == palindrome:
                # Check if this occurrence overlaps with used indices
                if not any(idx in used_indices for idx in range(i, i+len(palindrome))):
                    result.append(palindrome)
                    # Mark indices as used
                    used_indices.update(range(i, i+len(palindrome)))
                    break
    
    return sorted(result)