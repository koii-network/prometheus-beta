def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    This is a key preprocessing step in the KMP algorithm that helps 
    avoid unnecessary comparisons during string matching.
    
    Args:
        pattern (str): The pattern to be searched for
    
    Returns:
        list: LPS array containing longest proper prefix lengths
    """
    # Length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    
    # Length of the current longest prefix suffix
    length = 0
    
    # LPS array always starts with 0 for the first character
    i = 1
    
    while i < len(pattern):
        # If characters match, extend the current prefix
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length != 0:
                # Go back to the previous longest prefix suffix
                length = lps[length - 1]
            else:
                # If length is 0, set LPS to 0 and move to next character
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt string matching.
    
    Finds all occurrences of the pattern in the given text.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If either input is empty
    """
    # Strict type checking
    if not (isinstance(text, str) and isinstance(pattern, str)):
        raise TypeError("Both text and pattern must be strings")
    
    # Empty input handling
    if not pattern:
        return [] if text else []
    
    if not text:
        return []
    
    # Compute the LPS array for the pattern
    lps = compute_lps_array(pattern)
    
    # List to store all match indices
    matches = []
    
    # Pointers for text and pattern
    text_idx = 0
    pattern_idx = 0
    
    while text_idx < len(text):
        # If characters match, move both pointers forward
        if text[text_idx] == pattern[pattern_idx]:
            text_idx += 1
            pattern_idx += 1
        
        # If full pattern is matched, record the match
        if pattern_idx == len(pattern):
            matches.append(text_idx - pattern_idx)
            # Continue search from the last matched position
            pattern_idx = lps[pattern_idx - 1]
        
        # If characters don't match and we're not at the start of the pattern
        elif text_idx < len(text) and text[text_idx] != pattern[pattern_idx]:
            # If we're not at the start of the pattern, use LPS array
            if pattern_idx != 0:
                pattern_idx = lps[pattern_idx - 1]
            else:
                # If we're at the start of the pattern, move text pointer
                text_idx += 1
    
    return matches