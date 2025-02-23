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
    
    # Create first and last column
    sorted_chars = sorted(bwt_text)
    
    # Create mapping to track original rotations
    n = len(bwt_text)
    mapping = [0] * n
    
    # Build the mapping
    for i in range(n):
        char = bwt_text[i]
        mapping[i] = sorted_chars.index(char)
        sorted_chars[mapping[i]] = chr(ord(sorted_chars[mapping[i]]) + 1)
    
    # Reconstruct the original text
    current = mapping[0]
    result = [bwt_text[current]]
    
    for _ in range(n - 1):
        current = mapping[current]
        result.append(bwt_text[current])
    
    # Reverse and convert to string, removing the terminator
    original = ''.join(reversed(result))[:-1]
    
    return original