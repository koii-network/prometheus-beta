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
    
    # Find all palindromic substrings in the string
    def find_palindromes(string):
        palinds = []
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                substr = string[i:j]
                if substr == substr[::-1] and len(substr) > 1:
                    palinds.append((substr, i))
        return sorted(palinds, key=lambda x: (-len(x[0]), x[0]))
    
    # Find non-overlapping palindromes
    result = []
    used_indices = set()
    
    for pal, start in find_palindromes(s):
        # Check if the indices for this palindrome are free
        if not any(idx in used_indices for idx in range(start, start + len(pal))):
            result.append(pal)
            used_indices.update(range(start, start + len(pal)))
    
    # If no multi-character palindromes found, return empty list
    # Single characters are not considered palindromes in this context
    return result