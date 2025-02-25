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
    
    # Precompute first column (sorted characters)
    first_column = sorted(bwt_text)
    
    # Compute last-to-first mapping
    last_to_first = {}
    counts = {}
    
    for i, char in enumerate(bwt_text):
        if char not in counts:
            counts[char] = 0
        last_to_first[(char, counts[char])] = i
        counts[char] += 1
    
    # Initialize reconstruction
    current_index = first_column.index('$')
    reconstructed = []
    
    for _ in range(n - 1):
        # Append next character
        current_char = first_column[current_index]
        reconstructed.append(current_char)
        
        # Find the next index
        char_count = sum(1 for c in first_column[:current_index + 1] if c == current_char)
        current_index = last_to_first.get((current_char, char_count - 1), -1)
        
        if current_index == -1:
            break
    
    return ''.join(reconstructed)