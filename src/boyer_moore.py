def boyer_moore_search(text, pattern):
    """
    Implement the Boyer-Moore string searching algorithm.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    """
    # Preprocessing
    def bad_character_heuristic(pattern):
        """Create the bad character heuristic table."""
        # Initialize all occurrences as -1
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char
    
    # Edge cases
    if not pattern or not text:
        return []
    
    # Preprocess the pattern
    bad_char = bad_character_heuristic(pattern)
    
    # Result list to store all occurrences
    occurrences = []
    
    # Alignment of the pattern with the text
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        
        # Check characters from right to left
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        # If pattern is found
        if j < 0:
            occurrences.append(i)
            # Shift based on the pattern length if possible
            i += (len(pattern) - bad_char.get(text[i + len(pattern)], -1)) if i + len(pattern) < len(text) else 1
        else:
            # Use bad character heuristic to determine shift
            shift = max(1, j - bad_char.get(text[i + j], -1))
            i += shift
    
    return occurrences