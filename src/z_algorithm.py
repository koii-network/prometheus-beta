def z_algorithm(text, pattern):
    """
    Implement Z algorithm for string matching.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices where the pattern is found in the text
    """
    # Concatenate pattern and text with a delimiter
    search_string = pattern + "$" + text
    
    # Compute Z array
    z_array = [0] * len(search_string)
    left, right = 0, 0
    
    for k in range(1, len(search_string)):
        # If k is outside the Z-box, compute Z[k] normally
        if k > right:
            left = right = k
            while right < len(search_string) and search_string[right - left] == search_string[right]:
                right += 1
            z_array[k] = right - left
            right -= 1
        
        # If k is inside the Z-box
        else:
            # Check if the remaining interval needs to be expanded
            k1 = k - left
            
            # If the value does not stretch to the end of the Z-box, copy it
            if z_array[k1] < right - k + 1:
                z_array[k] = z_array[k1]
            
            # Otherwise, expand beyond the current Z-box
            else:
                left = k
                while right < len(search_string) and search_string[right - left] == search_string[right]:
                    right += 1
                z_array[k] = right - left
                right -= 1
    
    # Find indices where pattern is found (Z[i] == len(pattern))
    result = []
    pattern_length = len(pattern)
    for i in range(pattern_length + 1, len(search_string)):
        if z_array[i] == pattern_length:
            result.append(i - pattern_length - 1)
    
    return result