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
    
    # Find all possible palindromic substrings
    def find_all_palindromes(s: str) -> list[str]:
        return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if is_palindrome(s[i:j])]
    
    # Sort all palindromic substrings
    palindromes = sorted(set(find_all_palindromes(s)), key=len)
    
    # Non-overlapping algorithm
    result = []
    used_indices = set()
    
    for palindrome in palindromes:
        # Check if this palindrome overlaps with already used indices
        if not any(idx in used_indices for idx in range(s.index(palindrome), s.index(palindrome) + len(palindrome))):
            result.append(palindrome)
            # Mark the indices of this palindrome as used
            used_indices.update(range(s.index(palindrome), s.index(palindrome) + len(palindrome)))
    
    return sorted(result)