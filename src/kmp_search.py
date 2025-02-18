def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array 
    for the KMP algorithm.
    
    Args:
        pattern (str): The pattern string to compute LPS array for
    
    Returns:
        list: The LPS array
    """
    # Length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    length = 0  # Length of the current longest prefix suffix
    i = 1

    # LPS array computation
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # Try to find a shorter prefix
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
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        return []  # Empty pattern matches nowhere
    
    # Compute the LPS array
    lps = compute_lps_array(pattern)
    
    # KMP search
    matches = []
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        # If characters match, move both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # Pattern found
        if j == len(pattern):
            matches.append(i - j)
            # Continue searching by updating j
            j = lps[j-1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not at the start, use LPS array
            if j != 0:
                j = lps[j-1]
            else:
                # Otherwise move to next character in text
                i += 1
    
    return matches