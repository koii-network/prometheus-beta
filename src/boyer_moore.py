def boyer_moore_search(text, pattern):
    """
    Implement the Boyer-Moore string searching algorithm.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    """
    # Preprocessing: Build bad character heuristic
    def build_bad_character_table(pattern):
        bad_char = {}
        for i in range(len(pattern) - 1):
            bad_char[pattern[i]] = len(pattern) - 1 - i
        return bad_char
    
    # Preprocessing: Build good suffix heuristic
    def build_good_suffix_table(pattern):
        m = len(pattern)
        good_suffix = [0] * m
        last_prefix_position = m
        
        for i in range(m - 1, -1, -1):
            if is_prefix(pattern, i):
                last_prefix_position = i
            good_suffix[m - 1 - i] = last_prefix_position - i + m - 1
        
        for i in range(m - 1):
            suffix_length = longest_suffix_length(pattern, i)
            good_suffix[suffix_length] = m - 1 - i + suffix_length
        
        return good_suffix
    
    def is_prefix(pattern, p):
        for i in range(p, len(pattern)):
            if pattern[i] != pattern[i - p]:
                return False
        return True
    
    def longest_suffix_length(pattern, p):
        length = 0
        for i in range(p, len(pattern)):
            if pattern[i] == pattern[length]:
                length += 1
            else:
                break
        return length
    
    # Validate inputs
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        return []
    
    # Preprocessing
    bad_char = build_bad_character_table(pattern)
    good_suffix = build_good_suffix_table(pattern)
    
    # Search
    results = []
    m = len(pattern)
    n = len(text)
    
    i = 0
    while i <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        if j < 0:
            results.append(i)
            i += m - good_suffix[0] if m > 1 else 1
        else:
            # Calculate shifts using bad character and good suffix heuristics
            bad_char_shift = bad_char.get(text[i + j], m)
            good_suffix_shift = good_suffix[j]
            
            i += max(bad_char_shift, good_suffix_shift)
    
    return results