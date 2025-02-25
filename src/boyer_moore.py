def build_bad_character_table(pattern):
    """
    Build the bad character heuristic table for Boyer-Moore algorithm.
    
    Args:
        pattern (str): The pattern to search for.
    
    Returns:
        dict: A dictionary mapping characters to their rightmost position in the pattern.
    """
    bad_char = {}
    for i in range(len(pattern)):
        # Most recent occurrence of the character updates its position
        bad_char[pattern[i]] = i
    return bad_char

def boyer_moore_search(text, pattern):
    """
    Implement the Boyer-Moore string searching algorithm.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: A list of starting indices where the pattern is found in the text.
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be an empty string")
    
    # Special case: pattern longer than text
    if len(pattern) > len(text):
        return []
    
    # Build bad character table
    bad_char = build_bad_character_table(pattern)
    
    # Store found matches
    matches = []
    
    # Iterate through the text
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        
        # Try to match characters from right to left
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        # If pattern is found
        if j < 0:
            matches.append(i)
            # Shift pattern to the next valid position
            i += len(pattern) - bad_char.get(text[i + len(pattern)], -1) if i + len(pattern) < len(text) else 1
        else:
            # Shift pattern based on bad character heuristic
            char_shift = bad_char.get(text[i + j], -1)
            shift = max(1, j - char_shift)
            i += shift
    
    return matches