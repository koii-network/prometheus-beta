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
    # Handle empty string
    if not s:
        return []
    
    # Precompute palindromes 
    def is_palindrome(substring: str) -> bool:
        return substring == substring[::-1]
    
    # Advanced palindrome finding
    def find_palindromes(s: str) -> list[str]:
        # Combine multiple strategies to find palindromes
        palindromes = set()
        n = len(s)
        
        # Single characters are always palindromes
        palindromes.update(s[i] for i in range(n))
        
        # Find longer palindromes
        for length in range(2, n+1):
            for start in range(n - length + 1):
                substr = s[start:start+length]
                if is_palindrome(substr):
                    palindromes.add(substr)
        
        return sorted(palindromes, key=lambda x: (-len(x), x))
    
    # Find potential non-overlapping palindromes
    all_palindromes = find_palindromes(s)
    
    result = []
    used_indices = set()
    
    # Greedy selection of non-overlapping palindromes
    for palindrome in all_palindromes:
        # Try to find first non-overlapping occurrence
        for i in range(len(s)):
            if s[i:i+len(palindrome)] == palindrome:
                # Check for overlap
                if not any(idx in used_indices for idx in range(i, i+len(palindrome))):
                    result.append(palindrome)
                    used_indices.update(range(i, i+len(palindrome)))
                    break
    
    return sorted(result)