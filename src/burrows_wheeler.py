def burrows_wheeler_transform(input_text):
    """
    Perform the Burrows-Wheeler Transform on the input text.
    
    The Burrows-Wheeler Transform is a critical step in data compression 
    that rearranges the characters of a text to improve compression efficiency.
    
    Args:
        input_text (str): The input string to transform
    
    Returns:
        str: The Burrows-Wheeler transformed string
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Validate input
    if not isinstance(input_text, str):
        raise TypeError("Input must be a string")
    
    if not input_text:
        raise ValueError("Input string cannot be empty")
    
    # Add terminator character (typically '$')
    text = input_text + '$'
    
    # Generate all rotations of the text
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Extract the last character of each sorted rotation
    bwt_result = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return bwt_result

def inverse_burrows_wheeler_transform(bwt_text):
    """
    Perform the inverse Burrows-Wheeler Transform to recover the original text.
    
    Args:
        bwt_text (str): The Burrows-Wheeler transformed string
    
    Returns:
        str: The original text before transformation
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Validate input
    if not isinstance(bwt_text, str):
        raise TypeError("Input must be a string")
    
    if not bwt_text:
        raise ValueError("Input string cannot be empty")
    
    # Create the first column by sorting BWTransform
    first_column = sorted(list(bwt_text))
    
    # Track characters in columns 
    n = len(bwt_text)
    
    # Calculate the next array (mapping between columns)
    next_arr = [0] * n
    indices = {}
    
    for i, char in enumerate(first_column):
        # Handle first occurrence of char
        if char not in indices:
            indices[char] = 0
        
        # Find where this occurrence of char is in bwt_text
        for j in range(n):
            if bwt_text[j] == char and indices[char] == 0:
                next_arr[i] = j
                break
        
        # Increment count of this character
        indices[char] += 1
    
    # Start from the row with '$' terminator
    terminator_index = first_column.index('$')
    current = terminator_index
    
    # Reconstruct original string by tracing back
    result = []
    for _ in range(n):
        result.append(bwt_text[current])
        current = next_arr[current]
    
    # Convert back to original text (remove terminal '$')
    return ''.join(reversed(result))[:-1]