def burrows_wheeler_transform(input_text: str) -> str:
    """
    Implement the Burrows-Wheeler Transform for data compression.
    
    The Burrows-Wheeler Transform rearranges a block of data to improve 
    compression efficiency by grouping similar characters together.
    
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
    
    # Add terminator character to handle rotations
    modified_text = input_text + '$'
    
    # Generate all rotations of the text
    rotations = [modified_text[i:] + modified_text[:i] for i in range(len(modified_text))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Extract the last character of each sorted rotation
    bwt_result = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return bwt_result

def inverse_burrows_wheeler_transform(bwt_text: str) -> str:
    """
    Inverse Burrows-Wheeler Transform to recover the original text.
    
    Args:
        bwt_text (str): The Burrows-Wheeler transformed string
    
    Returns:
        str: The original text before transformation
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is empty or doesn't end with '$'
    """
    # Validate input
    if not isinstance(bwt_text, str):
        raise TypeError("Input must be a string")
    
    if not bwt_text:
        raise ValueError("Input string cannot be empty")
    
    # Ensure the terminator is present
    if '$' not in bwt_text:
        raise ValueError("Input must contain terminator character '$'")
    
    # Length of the text
    n = len(bwt_text)
    
    # Create first column and last column
    sorted_chars = sorted(bwt_text)
    
    # Compute next array to reconstruct the original text
    next_arr = [sorted_chars.index(c) for c in bwt_text]
    
    # Reconstruct the original text
    current = sorted_chars.index('$')
    result = []
    
    for _ in range(n - 1):
        result.append(bwt_text[current])
        current = next_arr[current]
    
    return ''.join(result)