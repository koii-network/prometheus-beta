def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    Args:
        pattern (str): The pattern to compute LPS array for
    
    Returns:
        list: LPS array indicating the longest proper prefix which is also a suffix
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
    Perform Knuth-Morris-Pratt (KMP) string matching algorithm.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be an empty string")
    
    # Compute the LPS array
    lps = compute_lps_array(pattern)
    
    # Matching results
    matches = []
    
    # Pointers
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        # If characters match, move both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # Pattern is fully matched
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If we have some matches, use LPS to skip comparisons
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches