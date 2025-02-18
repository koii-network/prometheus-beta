def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array 
    for the Knuth-Morris-Pratt (KMP) algorithm.
    
    Args:
        pattern (str): The pattern string to compute LPS array for
    
    Returns:
        list: LPS array where each index represents the length of the 
              longest proper prefix which is also a suffix for the 
              substring pattern[0:index+1]
    """
    # Length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    
    # LPS array always starts with 0
    i = 1
    
    while i < len(pattern):
        # If characters match, increment length and store in LPS array
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length != 0:
                # Go back to the previous prefix suffix length
                length = lps[length - 1]
            else:
                # If length is 0, set LPS[i] to 0 and move to next character
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt string matching algorithm.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: List of starting indices where the pattern is found in the text
    """
    # Edge cases
    if not pattern:
        return []
    if not text:
        return []
    
    # Compute the LPS array for the pattern
    lps = compute_lps_array(pattern)
    
    # Indices to track matching
    matches = []
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        # If characters match, move both indices forward
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # If full pattern is matched, record the match
        if j == len(pattern):
            matches.append(i - j)
            # Reset j to the LPS value to continue searching
            j = lps[j - 1]
        
        # If characters don't match
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not at the start, use LPS to skip characters
            if j != 0:
                j = lps[j - 1]
            else:
                # If j is at the start, move to next character in text
                i += 1
    
    return matches