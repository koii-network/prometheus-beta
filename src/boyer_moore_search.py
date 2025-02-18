def boyer_moore_search(text, pattern):
    """
    Implement the Boyer-Moore string search algorithm.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        return []
    
    # Preprocess: Create bad character rule table
    def create_bad_character_table(pattern):
        bad_char = {}
        for i in range(len(pattern) - 1):
            bad_char[pattern[i]] = len(pattern) - 1 - i
        return bad_char
    
    # Preprocess: Create good suffix rule table
    def create_good_suffix_table(pattern):
        m = len(pattern)
        good_suffix = [0] * m
        last_prefix_position = m
        
        for i in range(m - 1, -1, -1):
            if is_prefix(pattern, i):
                last_prefix_position = i
            
            good_suffix[m - 1 - i] = last_prefix_position - i + m - 1
        
        for i in range(m - 1):
            j = longest_proper_suffix_length(pattern, i)
            good_suffix[j] = m - 1 - i + j
        
        return good_suffix
    
    def is_prefix(pattern, p):
        j = 0
        for i in range(p, len(pattern)):
            if pattern[i] != pattern[j]:
                return False
            j += 1
        return True
    
    def longest_proper_suffix_length(pattern, p):
        m = len(pattern)
        length = 0
        j = m - 1
        
        while p >= 0 and pattern[p] == pattern[j]:
            length += 1
            p -= 1
            j -= 1
        
        return length
    
    # Main Boyer-Moore search
    bad_char_table = create_bad_character_table(pattern)
    good_suffix_table = create_good_suffix_table(pattern)
    
    m = len(pattern)
    n = len(text)
    results = []
    
    i = 0
    while i <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        if j < 0:
            results.append(i)
            # If at the end of text, stop
            i += m if i + m >= n else 1
        else:
            # Calculate shifts using bad character and good suffix rules
            bad_char_shift = bad_char_table.get(text[i + j], m)
            good_suffix_shift = good_suffix_table[m - 1 - j]
            
            # Take the maximum shift to ensure no missed matches
            i += max(1, bad_char_shift, good_suffix_shift)
    
    return results