def z_algorithm(text, pattern):
    """
    Implement the Z algorithm for string matching.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of indices where the pattern is found in the text
    """
    # Combine pattern and text with a separator 
    # to handle overlapping matches and track pattern positions
    search_string = pattern + '$' + text
    
    # Initialize Z array with zeros
    z = [0] * len(search_string)
    
    # Tracking for Z-box
    left, right = 0, 0
    
    # Results to store match indices
    matches = []
    
    # Compute Z array
    for k in range(1, len(search_string)):
        # If k is outside the current Z-box, compute Z[k] naively
        if k > right:
            left = right = k
            while right < len(search_string) and search_string[right - left] == search_string[right]:
                right += 1
            z[k] = right - left
            right -= 1
        else:
            # k is inside the Z-box
            k1 = k - left
            
            # If the remaining length fits inside the Z-box
            if z[k1] < right - k + 1:
                z[k] = z[k1]
            else:
                # Extend the Z-box
                left = k
                while right < len(search_string) and search_string[right - left] == search_string[right]:
                    right += 1
                z[k] = right - left
                right -= 1
        
        # Check if a match is found (full pattern length)
        if z[k] == len(pattern):
            matches.append(k - len(pattern) - 1)
    
    return matches