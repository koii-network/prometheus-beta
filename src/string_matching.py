def compute_lps_array(pattern: str) -> list:
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array
    for the Knuth-Morris-Pratt (KMP) algorithm.
    
    Args:
        pattern (str): The pattern string to compute LPS for
    
    Returns:
        list: The LPS array
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

def kmp_search(text: str, pattern: str) -> list:
    """
    Perform KMP (Knuth-Morris-Pratt) string matching algorithm.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    """
    # Handle edge cases
    if not pattern:
        return []
    
    # Compute the LPS array
    lps = compute_lps_array(pattern)
    
    # Result list to store match indices
    matches = []
    
    # Pointers for text and pattern
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        # If characters match, increment both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # Pattern fully matched
        if j == len(pattern):
            matches.append(i - j)
            # Reset j to the proper prefix length
            j = lps[j - 1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not at the start, use LPS array
            if j != 0:
                j = lps[j - 1]
            else:
                # No match, move to next character in text
                i += 1
    
    return matches