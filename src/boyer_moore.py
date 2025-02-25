def build_bad_character_table(pattern):
    """
    Build the bad character table for the Boyer-Moore algorithm.
    
    Args:
        pattern (str): The pattern to search for.
    
    Returns:
        dict: A dictionary mapping characters to their rightmost position 
              in the pattern (excluding the last occurrence).
    """
    bad_char = {}
    for i in range(len(pattern) - 1):
        bad_char[pattern[i]] = i
    return bad_char

def boyer_moore_search(text, pattern):
    """
    Implement the Boyer-Moore string matching algorithm.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: A list of starting indices where the pattern is found in the text.
        
    Raises:
        TypeError: If inputs are not strings.
        ValueError: If pattern is empty.
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    # If pattern is longer than text, no match is possible
    if len(pattern) > len(text):
        return []
    
    # Build bad character table
    bad_char = build_bad_character_table(pattern)
    
    # Store match indices
    matches = []
    
    # Current position in the text
    i = 0
    
    while i <= len(text) - len(pattern):
        # Starting from the rightmost character of the pattern
        j = len(pattern) - 1
        
        # Compare characters from right to left
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        # If pattern is found
        if j < 0:
            matches.append(i)
            # Shift to the next possible position
            i += len(pattern) - bad_char.get(text[i + len(pattern) - 1], -1) if i + len(pattern) < len(text) else 1
        else:
            # Use bad character heuristic to determine shift
            bad_char_shift = bad_char.get(text[i + j], -1)
            shift = max(1, j - bad_char_shift)
            i += shift
    
    return matches