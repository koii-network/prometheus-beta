def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array 
    for the Knuth-Morris-Pratt algorithm.
    
    Args:
        pattern (str): The pattern string to compute LPS for.
    
    Returns:
        list: The LPS array for the given pattern.
    """
    # Length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    length = 0  # Length of the current longest prefix suffix
    
    # Starting index for LPS computation
    i = 1
    
    # Compute LPS array
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            # If characters match, increment both length and index
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length != 0:
                # Go back to previous longest prefix suffix
                length = lps[length - 1]
            else:
                # If length is 0, set LPS for current index to 0
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt string matching.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: List of starting indices where the pattern is found in the text.
    """
    # Handle empty pattern or text cases
    if not pattern:
        return []
    if not text:
        return []
    
    # Compute the LPS array for the pattern
    lps = compute_lps_array(pattern)
    
    # Indices to track positions in text and pattern
    text_index = 0
    pattern_index = 0
    
    # List to store all starting indices of pattern matches
    matches = []
    
    while text_index < len(text):
        # If characters match, move both indices forward
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1
        
        # If full pattern is matched, record the match
        if pattern_index == len(pattern):
            matches.append(text_index - pattern_index)
            # Continue searching by updating pattern index
            pattern_index = lps[pattern_index - 1]
        
        # If characters don't match and we're not at the start of the pattern
        elif text_index < len(text) and text[text_index] != pattern[pattern_index]:
            # If pattern index is not 0, use LPS array to determine next position
            if pattern_index != 0:
                pattern_index = lps[pattern_index - 1]
            else:
                # If pattern index is 0, move to next character in text
                text_index += 1
    
    return matches