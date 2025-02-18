def z_algorithm(text, pattern):
    """
    Implement the Z algorithm for efficient string matching.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    """
    # Construct the combined string with a separator
    combined = pattern + '$' + text
    
    # Initialize Z array with zeros
    z = [0] * len(combined)
    
    # Variables to track the Z-box
    left, right = 0, 0
    
    # Calculate Z values
    for k in range(1, len(combined)):
        # If k is outside the current Z-box, compute Z[k] naively
        if k > right:
            left = right = k
            while right < len(combined) and combined[right - left] == combined[right]:
                right += 1
            z[k] = right - left
            right -= 1
        else:
            # k is inside the Z-box
            k1 = k - left
            
            # If the value does not stretch to the right edge of Z-box
            if z[k1] < right - k + 1:
                z[k] = z[k1]
            else:
                # Otherwise, recheck the remaining part
                left = k
                while right < len(combined) and combined[right - left] == combined[right]:
                    right += 1
                z[k] = right - left
                right -= 1
    
    # Find matches (where Z value equals pattern length)
    pattern_length = len(pattern)
    matches = []
    
    for i in range(pattern_length + 1, len(combined)):
        if z[i] == pattern_length:
            matches.append(i - pattern_length - 1)
    
    return matches