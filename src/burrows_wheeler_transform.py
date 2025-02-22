def burrows_wheeler_transform(text):
    """
    Perform the Burrows-Wheeler Transform on the input text.
    
    Args:
        text (str): The input string to transform.
    
    Returns:
        tuple: A tuple containing the transformed string and the original index.
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        return "", 0
    
    # Add a special terminator character that is lexicographically smaller than any other
    text_with_terminator = text + "$"
    
    # Generate all rotations of the text
    rotations = [text_with_terminator[i:] + text_with_terminator[:i] 
                 for i in range(len(text_with_terminator))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Find the original index (the position of the original text in sorted rotations)
    original_index = sorted_rotations.index(text_with_terminator)
    
    # Create the BWT by taking the last character of each sorted rotation
    bwt_result = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return bwt_result, original_index


def inverse_burrows_wheeler_transform(bwt_text, original_index):
    """
    Perform the inverse Burrows-Wheeler Transform to recover the original text.
    
    Args:
        bwt_text (str): The Burrows-Wheeler transformed text.
        original_index (int): The original index from the forward transform.
    
    Returns:
        str: The reconstructed original text.
    """
    # Validate input
    if not isinstance(bwt_text, str):
        raise TypeError("BWT text must be a string")
    
    if not isinstance(original_index, int):
        raise TypeError("Original index must be an integer")
    
    if not bwt_text:
        return ""
    
    # Create first column by sorting
    sorted_chars = sorted(bwt_text)
    
    # Create the next and last arrays
    next_array = {}
    for i, char in enumerate(bwt_text):
        if char not in next_array:
            next_array[char] = 0
        next_array[char] += 1
    
    # Reconstruct the original text
    result = []
    current_char = sorted_chars[original_index]
    count = 0
    
    while len(result) < len(bwt_text) - 1:  # Exclude terminator
        result.append(current_char)
        
        # Find the next character
        for i, char in enumerate(bwt_text):
            if char == current_char and count < next_array[char]:
                current_char = sorted_chars[i]
                count += 1
                break
    
    return ''.join(result[::-1])  # Reverse the result