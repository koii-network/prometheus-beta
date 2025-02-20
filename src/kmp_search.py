def compute_lps(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array
    for the Knuth-Morris-Pratt algorithm.
    
    Args:
        pattern (str): The pattern to search for
    
    Returns:
        list: LPS array for the given pattern
    """
    # Length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    length = 0  # Length of the current longest prefix suffix
    
    # The first character always has LPS of 0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            # If characters match, extend the current prefix
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length != 0:
                # Backtrack to the previous prefix 
                length = lps[length - 1]
            else:
                # No matching prefix, set LPS to 0
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt string search algorithm.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    """
    # Handle empty pattern or text cases
    if not pattern:
        return []
    if not text:
        return []
    
    # Compute the LPS array for the pattern
    lps = compute_lps(pattern)
    
    # Result list to store match indices
    matches = []
    
    # Pointers for text and pattern
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        # If characters match, move both pointers forward
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # If full pattern is matched, record the match
        if j == len(pattern):
            matches.append(i - j)
            # Continue searching by updating j to the LPS value
            j = lps[j - 1]
        
        # If characters don't match
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not at the start of the pattern, use LPS
            if j != 0:
                j = lps[j - 1]
            else:
                # Start checking from the beginning
                i += 1
    
    return matches