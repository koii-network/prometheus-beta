def z_algorithm(text, pattern):
    """
    Implement the Z algorithm for efficient string matching.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If inputs are empty strings
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Inputs must be strings")
    
    if not text or not pattern:
        raise ValueError("Inputs cannot be empty")
    
    # Combine pattern and text with a separator
    combined = pattern + '$' + text
    
    # Z-array computation
    z = [0] * len(combined)
    left, right = 0, 0
    
    # Compute Z-array
    for k in range(1, len(combined)):
        # If k is outside the current Z-box, compute Z[k] from scratch
        if k > right:
            left = right = k
            while right < len(combined) and combined[right - left] == combined[right]:
                right += 1
            z[k] = right - left
            right -= 1
        else:
            # We are inside the Z-box
            k1 = k - left
            
            # If the value does not stretch to the right edge of Z-box,
            # just copy the value
            if z[k1] < right - k + 1:
                z[k] = z[k1]
            else:
                # Otherwise, we need to do more comparisons
                left = k
                while right < len(combined) and combined[right - left] == combined[right]:
                    right += 1
                z[k] = right - left
                right -= 1
    
    # Find occurrences of the pattern
    occurrences = []
    pattern_length = len(pattern)
    
    for i in range(pattern_length + 1, len(combined)):
        if z[i] == pattern_length:
            occurrences.append(i - pattern_length - 1)
    
    return occurrences