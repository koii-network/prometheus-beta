def z_algorithm(text, pattern):
    """
    Implement the Z algorithm for efficient string matching.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    """
    if not text or not pattern:
        return []
    
    # Construct the Z string by combining pattern and text
    z_string = pattern + '$' + text
    
    # Initialize Z array
    z_array = [0] * len(z_string)
    
    # Variables to track the Z-box
    left, right = 0, 0
    
    # Compute Z array
    for k in range(1, len(z_string)):
        # If k is outside the current Z-box, compute Z[k] naively
        if k > right:
            left = right = k
            while right < len(z_string) and z_string[right - left] == z_string[right]:
                right += 1
            z_array[k] = right - left
            right -= 1
        else:
            # k is inside the Z-box
            k1 = k - left
            
            # If the value does not stretch to the right edge of Z-box, 
            # just copy the value
            if z_array[k1] < right - k + 1:
                z_array[k] = z_array[k1]
            else:
                # Otherwise, expand the Z-box
                left = k
                while right < len(z_string) and z_string[right - left] == z_string[right]:
                    right += 1
                z_array[k] = right - left
                right -= 1
    
    # Find all occurrences of the pattern
    results = []
    pattern_length = len(pattern)
    
    for i in range(pattern_length + 1, len(z_string)):
        if z_array[i] == pattern_length:
            results.append(i - pattern_length - 1)
    
    return results