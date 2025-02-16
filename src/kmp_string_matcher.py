def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    Args:
        pattern (str): The pattern to compute LPS array for
    
    Returns:
        list: LPS array for the given pattern
    """
    # Length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    
    # LPS array computation
    i = 1
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
    Perform Knuth-Morris-Pratt string matching.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    # Compute the Longest Prefix Suffix (LPS) array
    lps = compute_lps_array(pattern)
    
    # Results list to store all matches
    matches = []
    
    # Pointers
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        # If characters match, move both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # If pattern is fully matched, record the match
        if j == len(pattern):
            matches.append(i - j)
            # Move j to the proper position using LPS
            j = lps[j-1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not at the start, use LPS
            if j != 0:
                j = lps[j-1]
            else:
                # Otherwise, move to next character in text
                i += 1
    
    return matches