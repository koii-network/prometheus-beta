def compute_lps(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    Args:
        pattern (str): The pattern string to compute LPS for.
    
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
    Perform KMP (Knuth-Morris-Pratt) string matching algorithm.
    
    Args:
        text (str): The main text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: Indices of all occurrences of the pattern in the text.
    """
    if not pattern:
        return []
    
    # Compute the LPS array
    lps = compute_lps(pattern)
    
    # Initialize variables
    text_index = 0
    pattern_index = 0
    matches = []
    
    while text_index < len(text):
        # If characters match, move both indices forward
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1
        
        # If full pattern is matched, add to matches
        if pattern_index == len(pattern):
            matches.append(text_index - pattern_index)
            pattern_index = lps[pattern_index - 1]
        
        # If characters don't match and there are still characters left
        elif text_index < len(text) and text[text_index] != pattern[pattern_index]:
            # If pattern index is not at the start, use LPS array
            if pattern_index != 0:
                pattern_index = lps[pattern_index - 1]
            # If pattern index is at the start, move text index
            else:
                text_index += 1
    
    return matches