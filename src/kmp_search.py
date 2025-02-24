def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    This is a helper function for the KMP algorithm that precomputes 
    the longest prefix which is also a suffix for each prefix of the pattern.
    
    Args:
        pattern (str): The pattern to compute LPS array for
    
    Returns:
        list: LPS array containing longest prefix suffix lengths
    """
    # Handle empty pattern
    if not pattern:
        return []
    
    # Length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    length = 0  # Length of the current longest prefix suffix
    i = 1
    
    # LPS[0] is always 0
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            # If characters match, extend the prefix
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length != 0:
                # Go back to the previous longest prefix suffix
                length = lps[length - 1]
            else:
                # If length is 0, set LPS[i] to 0
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt string search algorithm.
    
    Finds all occurrences of a pattern within a text.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    # Handle empty pattern or text
    if not pattern or not text:
        return []
    
    # If pattern is longer than text, no match is possible
    if len(pattern) > len(text):
        return []
    
    # Compute the LPS array
    lps = compute_lps_array(pattern)
    
    # Results list to store match indices
    matches = []
    
    # Pointers for text and pattern
    i = 0  # text index
    j = 0  # pattern index
    
    while i < len(text):
        # If characters match, move both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # If full pattern is matched, record the match
        if j == len(pattern):
            matches.append(i - j)
            # Move j back using LPS array
            j = lps[j-1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not at the start, use LPS array
            if j != 0:
                j = lps[j-1]
            # If j is at the start, move text pointer
            else:
                i += 1
    
    return matches