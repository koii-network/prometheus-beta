def compute_lps_array(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array for KMP algorithm.
    
    Args:
        pattern (str): The pattern string to compute LPS array for.
    
    Returns:
        list: The LPS array for the given pattern.
    """
    lps = [0] * len(pattern)
    length = 0
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
    Perform Knuth-Morris-Pratt (KMP) string matching.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: List of starting indices where the pattern is found in the text.
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be an empty string")
    
    # Compute the LPS array
    lps = compute_lps_array(pattern)
    
    # Results storage
    matches = []
    
    # Matching process
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            # Pattern found
            matches.append(i - j)
            j = lps[j - 1]
        
        # Mismatch after j matches
        elif i < len(text) and pattern[j] != text[i]:
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches