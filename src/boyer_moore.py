def boyer_moore_search(text, pattern):
    """
    Implement the Boyer-Moore string searching algorithm.
    
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
    
    # Bad character heuristic
    def compute_bad_char_table(pattern):
        bad_char = {}
        for i in range(len(pattern) - 1):
            bad_char[pattern[i]] = len(pattern) - 1 - i
        return bad_char
    
    # Good suffix heuristic
    def compute_good_suffix_table(pattern):
        m = len(pattern)
        good_suffix = [0] * m
        last_prefix_pos = m
        
        for i in range(m - 1, -1, -1):
            if is_prefix(pattern, i):
                last_prefix_pos = i
            
            good_suffix[m - 1 - i] = last_prefix_pos - i + m - 1
        
        for i in range(m):
            if good_suffix[i] == m:
                good_suffix[i] = 0
        
        return good_suffix
    
    def is_prefix(pattern, pos):
        j = 0
        for i in range(pos, len(pattern)):
            if pattern[i] != pattern[j]:
                return False
            j += 1
        return True
    
    # Main Boyer-Moore search
    result = []
    m = len(pattern)
    n = len(text)
    
    if m > n:
        return result
    
    # Preprocess pattern
    bad_char = compute_bad_char_table(pattern)
    good_suffix = compute_good_suffix_table(pattern)
    
    i = 0
    while i <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        if j < 0:
            result.append(i)
            # Shift based on good suffix
            i += (m - good_suffix[0] if i + m < n else 1)
        else:
            # Use max of bad character and good suffix shifts
            bad_char_shift = bad_char.get(text[i + j], m)
            good_suffix_shift = good_suffix[m - 1 - j]
            i += max(bad_char_shift, good_suffix_shift)
    
    return result