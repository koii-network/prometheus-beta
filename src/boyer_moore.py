def boyer_moore_search(text, pattern):
    """
    Implement Boyer-Moore string matching algorithm.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    """
    # Handle empty inputs
    if not text or not pattern:
        return []
    
    # Preprocessing: Create bad character heuristic
    def create_bad_character_table(pattern):
        bad_char = {}
        for i in range(len(pattern) - 1):
            bad_char[pattern[i]] = len(pattern) - i - 1
        return bad_char
    
    # Preprocessing: Create good suffix heuristic
    def create_good_suffix_table(pattern):
        m = len(pattern)
        good_suffix = [0] * m
        last_prefix_position = m
        
        for i in range(m - 1, -1, -1):
            if pattern[:m-i] == pattern[i:]:
                last_prefix_position = i
            good_suffix[i] = last_prefix_position
        
        return good_suffix
    
    # Main Boyer-Moore search
    matches = []
    m = len(pattern)
    n = len(text)
    
    bad_char_table = create_bad_character_table(pattern)
    good_suffix_table = create_good_suffix_table(pattern)
    
    i = 0
    while i <= n - m:
        j = m - 1
        
        # Compare characters from right to left
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        # If pattern matches
        if j < 0:
            matches.append(i)
            # Shift based on good suffix heuristic
            i += m - good_suffix_table[0] if m > 1 else 1
        else:
            # Calculate shift based on bad character and good suffix heuristics
            bad_char_shift = bad_char_table.get(text[i + j], m)
            good_suffix_shift = good_suffix_table[j]
            i += max(bad_char_shift, good_suffix_shift)
    
    return matches