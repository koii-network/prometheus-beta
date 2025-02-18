def z_algorithm(s):
    """
    Implement the Z algorithm for string matching.
    
    The Z algorithm creates a Z array where Z[i] represents the length of the longest prefix 
    starting at index i that is also a prefix of the entire string.
    
    Args:
        s (str): The input string to compute Z values for
    
    Returns:
        list: Z array containing prefix match lengths
    
    Raises:
        TypeError: If input is not a string
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty list
    if not s:
        return []
    
    # Initialize Z array with length of string
    n = len(s)
    Z = [0] * n
    
    # First element is always the length of the entire string
    Z[0] = n
    
    # Tracking variables for Z-box
    left, right = 0, 0
    
    # Compute Z values
    for k in range(1, n):
        # Case 1: k is outside the current Z-box
        if k > right:
            # Naive comparison
            zk = 0
            while k + zk < n and s[zk] == s[k + zk]:
                zk += 1
            Z[k] = zk
            
            # Update Z-box if necessary
            if zk > 0:
                left = k
                right = k + zk - 1
        
        # Case 2: k is inside the current Z-box
        else:
            # Find corresponding index in prefix
            k1 = k - left
            
            # If the value does not stretch to the Z-box boundary
            if Z[k1] < right - k + 1:
                Z[k] = Z[k1]
            
            # If the value stretches beyond the Z-box boundary
            else:
                zk = right - k + 1
                while k + zk < n and s[zk] == s[k + zk]:
                    zk += 1
                Z[k] = zk
                
                # Update Z-box
                left = k
                right = k + zk - 1
    
    return Z

def find_pattern(text, pattern):
    """
    Find all occurrences of a pattern in a text using Z algorithm.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices where the pattern starts in the text
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Validate inputs
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    # If pattern is empty or longer than text, return empty list
    if not pattern or len(pattern) > len(text):
        return []
    
    # Concatenate pattern and text with a separator
    concat = pattern + '$' + text
    
    # Compute Z array
    z_arr = z_algorithm(concat)
    
    # Find pattern occurrences
    result = []
    for i in range(len(pattern) + 1, len(concat)):
        if z_arr[i] == len(pattern):
            result.append(i - len(pattern) - 1)
    
    return result