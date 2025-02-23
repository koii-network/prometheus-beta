def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also a Suffix (LPS) array.
    
    This is a key preprocessing step in the Knuth-Morris-Pratt algorithm 
    that helps to skip unnecessary comparisons during string matching.
    
    Args:
        pattern (str): The pattern string to compute LPS for
    
    Returns:
        list: LPS array where each index represents the length of the longest 
              proper prefix which is also a suffix for the substring 
              pattern[0:index+1]
    """
    # Initialize LPS array with 0s
    lps = [0] * len(pattern)
    
    # Length of the previous longest prefix suffix
    length = 0
    
    # Current index in pattern
    i = 1
    
    # Compute LPS array
    while i < len(pattern):
        # If characters match, extend the prefix
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        
        # If characters don't match and there's a previous prefix
        elif length > 0:
            # Move to the previous prefix length
            length = lps[length - 1]
        
        # No matching prefix found
        else:
            lps[i] = 0
            i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt string matching to find all occurrences 
    of a pattern within a text.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all starting positions where the pattern is found in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If either input is empty
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not text or not pattern:
        raise ValueError("Neither text nor pattern can be empty")
    
    # Compute the LPS array for the pattern
    lps = compute_lps_array(pattern)
    
    # List to store matching indices
    matches = []
    
    # Indices for text and pattern
    text_idx = 0
    pattern_idx = 0
    
    # Traverse through the text
    while text_idx < len(text):
        # Characters match, move both indices
        if text[text_idx] == pattern[pattern_idx]:
            text_idx += 1
            pattern_idx += 1
        
        # Full pattern match found
        if pattern_idx == len(pattern):
            matches.append(text_idx - pattern_idx)
            # Continue searching by updating pattern index
            pattern_idx = lps[pattern_idx - 1]
        
        # Mismatch after some matches
        elif text_idx < len(text) and text[text_idx] != pattern[pattern_idx]:
            # If we've made some progress in pattern, use LPS
            if pattern_idx > 0:
                pattern_idx = lps[pattern_idx - 1]
            # Otherwise, move text index
            else:
                text_idx += 1
    
    return matches