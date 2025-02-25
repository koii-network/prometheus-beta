def z_algorithm(text, pattern):
    """
    Implement the Z algorithm for string matching.
    
    The Z algorithm finds all occurrences of a pattern within a text in O(n+m) time complexity.
    
    Args:
        text (str): The full text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If inputs are empty strings
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not text or not pattern:
        raise ValueError("Text and pattern cannot be empty")
    
    # Construct Z array
    def compute_z_array(s):
        n = len(s)
        z = [0] * n
        left, right = 0, 0
        
        for k in range(1, n):
            # If k is outside the current Z-box, compute Z[k] from scratch
            if k > right:
                left = right = k
                while right < n and s[right - left] == s[right]:
                    right += 1
                z[k] = right - left
                right -= 1
            else:
                # k is inside the Z-box
                k1 = k - left
                
                # If the value does not stretch to the right edge of Z-box, 
                # just copy the value
                if z[k1] < right - k + 1:
                    z[k] = z[k1]
                else:
                    # Otherwise, extend the Z-box
                    left = k
                    while right < n and s[right - left] == s[right]:
                        right += 1
                    z[k] = right - left
                    right -= 1
        
        return z
    
    # Concatenate pattern and text with a delimiter
    search_string = pattern + '$' + text
    
    # Compute Z array for the concatenated string
    z_array = compute_z_array(search_string)
    
    # Find matches
    matches = []
    pattern_length = len(pattern)
    
    for i in range(pattern_length + 1, len(search_string)):
        if z_array[i] == pattern_length:
            matches.append(i - pattern_length - 1)
    
    return matches