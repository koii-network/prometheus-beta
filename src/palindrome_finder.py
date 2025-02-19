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
    
    # Find all palindromic substrings
    def all_palindromes(s):
        palinds = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr == substr[::-1]:
                    palinds.append(substr)
        return sorted(set(palinds), key=lambda x: (len(x), x), reverse=True)
    
    # Find non-overlapping palindromes
    def find_non_overlapping(palindromes):
        result = []
        used_indices = set()
        
        for pal in palindromes:
            # Find the first occurrence of the palindrome
            start = s.index(pal)
            
            # Check if indices are already used
            if any(idx in used_indices for idx in range(start, start + len(pal))):
                continue
            
            # Add palindrome and mark its indices as used
            result.append(pal)
            used_indices.update(range(start, start + len(pal)))
        
        return sorted(result)
    
    # Find and return non-overlapping palindromes
    return find_non_overlapping(all_palindromes(s))