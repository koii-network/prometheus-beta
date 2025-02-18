def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also a Suffix (LPS) array.
    
    Args:
        pattern (str): The pattern string to compute LPS for.
    
    Returns:
        list: LPS array for the given pattern.
    """
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform KMP (Knuth-Morris-Pratt) string search algorithm.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: List of starting indices where the pattern is found in the text.
    """
    if not pattern:
        return []
    
    if not text:
        return []

    # Compute the LPS array
    lps = compute_lps_array(pattern)
    
    results = []
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            # Pattern found
            results.append(i - j)
            j = lps[j - 1]
        
        # Mismatch after j matches
        elif i < len(text) and pattern[j] != text[i]:
            # Do not match lps[0..lps[j-1]] characters
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return results