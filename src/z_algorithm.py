def z_algorithm(text, pattern):
    """
    Implements the Z algorithm for string matching.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    """
    # Combine pattern and text with a separator
    search_string = pattern + '$' + text
    
    # Calculate Z array
    z = [0] * len(search_string)
    left, right = 0, 0
    
    for k in range(1, len(search_string)):
        # If k is outside the current Z-box, compute Z[k] normally
        if k > right:
            left = right = k
            while right < len(search_string) and search_string[right - left] == search_string[right]:
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
                # Otherwise, need to do more comparisons
                left = k
                while right < len(search_string) and search_string[right - left] == search_string[right]:
                    right += 1
                z[k] = right - left
                right -= 1
    
    # Find all occurrences of the pattern
    results = []
    for i in range(len(pattern) + 1, len(search_string)):
        if z[i] == len(pattern):
            results.append(i - len(pattern) - 1)
    
    return results