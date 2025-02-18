def z_algorithm(text, pattern):
    """
    Implement the Z algorithm for string matching.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    """
    # Combine pattern and text with a separator
    combined = pattern + '$' + text
    
    # Compute Z array
    z = [0] * len(combined)
    left, right = 0, 0
    
    for k in range(1, len(combined)):
        # If k is outside the Z-box, compute Z value from scratch
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
                # Compute additional matches
                left = k
                while right < len(combined) and combined[right - left] == combined[right]:
                    right += 1
                z[k] = right - left
                right -= 1
    
    # Find occurrences of the pattern
    pattern_length = len(pattern)
    occurrences = []
    
    for i in range(pattern_length + 1, len(combined)):
        if z[i] == pattern_length:
            occurrences.append(i - pattern_length - 1)
    
    return occurrences