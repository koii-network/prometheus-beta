def find_non_overlapping_palindromic_substrings(s):
    """
    Find and return all non-overlapping palindromic substrings of an input string,
    sorted in lexicographic order.
    
    Args:
        s (str): Input string to find palindromic substrings
    
    Returns:
        list: Sorted list of non-overlapping palindromic substrings
    """
    def is_palindrome(substring):
        """Check if a substring is a palindrome."""
        return substring == substring[::-1]
    
    if not s:
        return []
    
    # Find all palindromic substrings
    palindromes = []
    n = len(s)
    
    # Iterate through all possible substrings
    for start in range(n):
        for end in range(start + 1, n + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.append(substring)
    
    # Sort the palindromes lexicographically
    palindromes.sort()
    
    # Remove overlapping palindromes
    non_overlapping = []
    used_indices = set()
    
    for p in palindromes:
        # Find all occurrences of the palindrome
        start_indices = [i for i in range(len(s)) if s.startswith(p, i)]
        
        for idx in start_indices:
            # Check if this occurrence overlaps with previously used indices
            if not any(idx <= used_idx < idx + len(p) or 
                       idx <= used_idx < idx + len(p) for used_idx in used_indices):
                non_overlapping.append(p)
                used_indices.update(range(idx, idx + len(p)))
                break
    
    # Remove duplicates while preserving order
    result = []
    seen = set()
    for p in non_overlapping:
        if p not in seen:
            result.append(p)
            seen.add(p)
    
    return result