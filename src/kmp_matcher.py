def compute_lps(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    This is a key preprocessing step in the KMP algorithm that helps 
    avoid unnecessary comparisons during string matching.
    
    Args:
        pattern (str): The pattern string to compute LPS for
    
    Returns:
        list: An array of longest proper prefix lengths
    
    Raises:
        TypeError: If input is not a string
    """
    # Input validation
    if not isinstance(pattern, str):
        raise TypeError("Pattern must be a string")
    
    # Initialize LPS array with 0s
    lps = [0] * len(pattern)
    
    # Length of the previous longest prefix suffix
    length = 0
    i = 1
    
    # Compute LPS array
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length != 0:
                # Go back to the previous prefix
                length = lps[length - 1]
            else:
                # No prefix found
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt (KMP) string matching.
    
    Finds all occurrences of a pattern within a text.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all pattern occurrences in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is empty
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    # Edge case: pattern longer than text
    if len(pattern) > len(text):
        return []
    
    # Compute the LPS array for the pattern
    lps = compute_lps(pattern)
    
    # Results list to store match indices
    matches = []
    
    # Pointers for text and pattern
    i = 0  # text pointer
    j = 0  # pattern pointer
    
    while i < len(text):
        # If characters match, move both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # Pattern fully matched
        if j == len(pattern):
            matches.append(i - j)
            # Continue searching by updating j
            j = lps[j-1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not at the start, use LPS
            if j != 0:
                j = lps[j-1]
            else:
                # No match, move text pointer
                i += 1
    
    return matches