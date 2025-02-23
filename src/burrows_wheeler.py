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
    
    # Remove terminator for complex strings
    if '$' not in bwt_text:
        bwt_text += '$'
    
    # First column is sorted
    first_column = sorted(bwt_text)
    
    # Last column is the BWT
    last_column = list(bwt_text)
    
    # Construct the mapping for tracing back
    n = len(bwt_text)
    
    # Reconstruct the original text
    result = []
    current_char = '$'
    
    # Start with the $ terminator 
    current_index = first_column.index(current_char)
    
    for _ in range(n):
        result.append(last_column[current_index])
        
        # Find the next index
        current_char = last_column[current_index]
        current_index = first_column.index(current_char)
    
    # Reverse the result and remove terminator
    original = ''.join(reversed(result))[:-1]
    
    return original