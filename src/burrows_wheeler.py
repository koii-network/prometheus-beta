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
    
    # Create all cyclic rotations
    rotations = []
    for i in range(len(modified_text)):
        rotation = modified_text[i:] + modified_text[:i]
        rotations.append(rotation)
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Take the last column of the sorted matrix
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
        ValueError: If input is empty or doesn't contain '$'
    """
    # Validate input
    if not isinstance(bwt_text, str):
        raise TypeError("Input must be a string")
    
    if not bwt_text:
        raise ValueError("Input string cannot be empty")
    
    # Ensure the terminator is present
    if '$' not in bwt_text:
        raise ValueError("Input must contain terminator character '$'")
    
    # First column (sorted characters)
    first_column = sorted(bwt_text)
    
    # Create next/last column mapping
    n = len(bwt_text)
    last_to_first = {}
    for i in range(n):
        if bwt_text[i] not in last_to_first:
            last_to_first[bwt_text[i]] = 0
        last_to_first[bwt_text[i]] += 1
    
    # Reconstruct the original string
    current_char_index = first_column.index('$')
    result = []
    
    for _ in range(n - 1):
        # Find the next character by looking up in the last column
        result.append(first_column[current_char_index])
        
        # Update current index
        current_first_col_char_count = first_column[:current_char_index + 1].count(first_column[current_char_index])
        current_last_col_char_count = bwt_text[:current_char_index + 1].count(first_column[current_char_index])
        
        current_char_index = first_column.index(
            first_column[current_char_index], 
            current_first_col_char_count - current_last_col_char_count
        )
    
    return ''.join(result)