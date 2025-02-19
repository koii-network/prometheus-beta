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
    
    # Helper function to find all palindromes
    def find_palindromes(string):
        palinds = []
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                substr = string[i:j]
                if substr == substr[::-1]:
                    palinds.append(substr)
        return sorted(set(palinds), key=lambda x: (len(x), x), reverse=True)
    
    # Find non-overlapping palindromes
    def find_non_overlapping(palindromes):
        result = []
        used_indices = set()
        
        for pal in palindromes:
            # Find all occurrences of the palindrome
            occurrences = []
            start = 0
            while True:
                try:
                    index = s.index(pal, start)
                    occurrences.append(index)
                    start = index + 1
                except ValueError:
                    break
            
            # Try each occurrence
            for start in occurrences:
                # Check if indices are not used
                if not any(idx in used_indices for idx in range(start, start + len(pal))):
                    # Add palindrome and mark its indices
                    result.append(pal)
                    used_indices.update(range(start, start + len(pal)))
                    break
        
        return sorted(result)
    
    # Get palindromes, filter non-overlapping
    palindromes = find_palindromes(s)
    return find_non_overlapping(palindromes)