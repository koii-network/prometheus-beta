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
    
    # Single-character case
    if len(s) == 1:
        return [s]
    
    # Find all palindromic substrings in the string
    def find_palindromes(string):
        palinds = []
        for length in range(len(string), 0, -1):
            for i in range(len(string) - length + 1):
                substr = string[i:i+length]
                if substr == substr[::-1]:
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
            
            # Stop if we've found a satisfactory result
            if len(result) > 0:
                break
    
    return result