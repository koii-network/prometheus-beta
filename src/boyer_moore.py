def boyer_moore_search(text, pattern):
    """
    Implement the Boyer-Moore string searching algorithm.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    """
    # Edge cases
    if not pattern or not text:
        return []
    
    # Preprocessing: Bad Character Heuristic
    def bad_character_heuristic(pattern):
        # Create a dictionary to store the rightmost occurrence of each character
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char
    
    # Create bad character table
    bad_char = bad_character_heuristic(pattern)
    
    # Matching process
    matches = []
    m, n = len(pattern), len(text)
    i = 0  # index for text
    
    while i <= n - m:
        j = m - 1  # index for pattern, start from end
        
        # Try to match characters from right to left
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        # If pattern is found
        if j < 0:
            matches.append(i)
            # Shift by 1 if we're at the end, otherwise use bad character heuristic
            i += (m - bad_char.get(text[i + m], -1)) if i + m < n else 1
        else:
            # Use bad character heuristic to determine shift
            char_shift = j - bad_char.get(text[i + j], -1)
            i += max(1, char_shift)
    
    return matches