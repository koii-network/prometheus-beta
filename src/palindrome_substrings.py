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
    
    # Precompute all palindromes in descending length order
    def is_palindrome(substring: str) -> bool:
        return substring == substring[::-1]
    
    # Find all palindromic substrings, sorted by length (descending) and lexicographically
    all_palindromes = sorted(
        (substr for substr in set(s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if is_palindrome(s[i:j])),
        key=lambda x: (-len(x), x)
    )
    
    # Non-overlapping selection
    result = []
    used_indices = set()
    
    for palindrome in all_palindromes:
        # Find all occurrences of the palindrome
        start_idx = 0
        while True:
            # Find next occurrence of palindrome
            idx = s.find(palindrome, start_idx)
            
            # Stop if no more occurrences or palindrome not found
            if idx == -1:
                break
            
            # Check if this occurrence overlaps with used indices
            if not any(i in used_indices for i in range(idx, idx + len(palindrome))):
                result.append(palindrome)
                # Mark indices as used
                used_indices.update(range(idx, idx + len(palindrome)))
                break
            
            # Move start index to continue searching
            start_idx = idx + 1
    
    return sorted(result)