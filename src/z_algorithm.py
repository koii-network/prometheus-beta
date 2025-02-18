def z_algorithm(text, pattern):
    """
    Implement the Z algorithm for string matching.
    
    The Z algorithm finds all occurrences of a pattern within a text.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices where the pattern is found in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If inputs are empty strings
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not text or not pattern:
        raise ValueError("Text and pattern cannot be empty")
    
    # Combine pattern and text with a special delimiter
    z_string = pattern + '$' + text
    
    # Initialize Z array
    z_array = [0] * len(z_string)
    
    # Z algorithm implementation
    left, right = 0, 0
    for k in range(1, len(z_string)):
        # If k is outside the current Z-box, reset
        if k > right:
            left = right = k
            
            # Calculate Z value for this position
            while right < len(z_string) and z_string[right - left] == z_string[right]:
                right += 1
            
            z_array[k] = right - left
            right -= 1
        
        # If k is inside the Z-box
        else:
            # Check if we can reuse previously computed Z value
            k1 = k - left
            
            # If the value does not stretch to the right end of Z-box
            if z_array[k1] < right - k + 1:
                z_array[k] = z_array[k1]
            
            # Otherwise, we need to do more comparisons
            else:
                left = k
                while right < len(z_string) and z_string[right - left] == z_string[right]:
                    right += 1
                
                z_array[k] = right - left
                right -= 1
    
    # Find all occurrences of pattern
    occurrences = []
    pattern_length = len(pattern)
    for i in range(pattern_length + 1, len(z_string)):
        if z_array[i] == pattern_length:
            occurrences.append(i - pattern_length - 1)
    
    return occurrences