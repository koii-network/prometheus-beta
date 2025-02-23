def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    This is a key preprocessing step in the KMP algorithm that helps 
    avoid unnecessary comparisons during string matching.
    
    Args:
        pattern (str): The pattern string to compute LPS for
    
    Returns:
        list: LPS array where each index represents the length of the 
              longest proper prefix which is also a suffix for the 
              substring pattern[0:i+1]
    
    Time Complexity: O(m), where m is the length of the pattern
    Space Complexity: O(m)
    """
    # Initialize LPS array with 0s
    lps = [0] * len(pattern)
    
    # Length of the previous longest prefix suffix
    length = 0
    
    # Starting index for LPS computation
    i = 1
    
    # Compute LPS array
    while i < len(pattern):
        # If characters match, extend the prefix
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # If no match and we're not at the start
            if length != 0:
                # Go back in the LPS array
                length = lps[length - 1]
            else:
                # No match found, set LPS to 0
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform KMP (Knuth-Morris-Pratt) string matching.
    
    Finds all occurrences of the pattern in the given text.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all starting positions where pattern is found in text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is empty
    
    Time Complexity: O(n+m), where n is text length, m is pattern length
    Space Complexity: O(m)
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    # If pattern is longer than text, no match possible
    if len(pattern) > len(text):
        return []
    
    # Compute LPS array for the pattern
    lps = compute_lps_array(pattern)
    
    # Result list to store match indices
    matches = []
    
    # Indices for text and pattern
    i = 0  # text index
    j = 0  # pattern index
    
    while i < len(text):
        # If characters match, move both indices forward
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # If full pattern is matched, record the match
        if j == len(pattern):
            matches.append(i - j)
            # Continue matching by updating j using LPS
            j = lps[j-1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not at start, use LPS to determine next match position
            if j != 0:
                j = lps[j-1]
            else:
                # If j is at start, simply move text index
                i += 1
    
    return matches