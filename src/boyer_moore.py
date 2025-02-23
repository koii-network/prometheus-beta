def build_bad_character_table(pattern):
    """
    Build the bad character table for Boyer-Moore algorithm.
    
    Args:
        pattern (str): The pattern to search for.
    
    Returns:
        dict: A dictionary mapping characters to their rightmost occurrence in the pattern.
    """
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char

def build_good_suffix_table(pattern):
    """
    Build the good suffix table for Boyer-Moore algorithm.
    
    Args:
        pattern (str): The pattern to search for.
    
    Returns:
        list: A list of shifts for good suffix rule.
    """
    m = len(pattern)
    good_suffix = [0] * m
    last_prefix_pos = m
    
    for i in range(m - 1, -1, -1):
        if pattern[i:] == pattern[m - len(pattern[i:]):]:
            last_prefix_pos = i
        good_suffix[i] = last_prefix_pos
    
    return good_suffix

def boyer_moore_search(text, pattern):
    """
    Perform Boyer-Moore string matching.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: Indices of all occurrences of the pattern in the text.
    """
    # Handle edge cases
    if not pattern:
        return []
    if not text:
        return []
    
    # Preprocessing
    m = len(pattern)
    n = len(text)
    
    # Build tables
    bad_char = build_bad_character_table(pattern)
    good_suffix = build_good_suffix_table(pattern)
    
    # Search
    matches = []
    i = 0  # index for text
    while i <= n - m:
        j = m - 1  # index for pattern (right to left)
        
        # Try to match characters from right to left
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        # If pattern is matched
        if j < 0:
            matches.append(i)
            # For overlapping matches, shift by 1
            i += 1
        else:
            # Calculate shifts
            bad_char_shift = j - bad_char.get(text[i + j], -1)
            good_suffix_shift = 0
            if j < m - 1:
                good_suffix_shift = m - 1 - good_suffix[j + 1]
            
            # Take the maximum shift
            shift = max(1, bad_char_shift, good_suffix_shift)
            i += shift
    
    return matches