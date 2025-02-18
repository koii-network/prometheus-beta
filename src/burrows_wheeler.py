def burrows_wheeler_transform(text):
    """
    Perform the Burrows-Wheeler Transform on the input text.
    
    Args:
        text (str): The input string to be transformed.
    
    Returns:
        tuple: A tuple containing the transformed string and the original index.
    
    Raises:
        ValueError: If the input is not a string or is an empty string.
    """
    # Input validation
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    if not text:
        raise ValueError("Input string cannot be empty")
    
    # Generate all rotations of the input text
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Find the original index and construct the transformed string
    original_index = sorted_rotations.index(text)
    transformed = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return transformed, original_index

def inverse_burrows_wheeler_transform(transformed_text, original_index):
    """
    Perform the inverse Burrows-Wheeler Transform.
    
    Args:
        transformed_text (str): The Burrows-Wheeler transformed string.
        original_index (int): The original index from the forward transform.
    
    Returns:
        str: The original input text.
    
    Raises:
        ValueError: If inputs are invalid.
    """
    # Input validation
    if not isinstance(transformed_text, str):
        raise ValueError("Transformed text must be a string")
    
    if not isinstance(original_index, int):
        raise ValueError("Original index must be an integer")
    
    if original_index < 0 or original_index >= len(transformed_text):
        raise ValueError("Invalid original index")
    
    # Create first and last column
    n = len(transformed_text)
    first_column = sorted(transformed_text)
    
    # Reconstruct the original text
    next_char_map = {char: first_column.count(char) for char in set(first_column)}
    
    reconstructed = [''] * n
    current_index = original_index
    
    for i in range(n - 1, -1, -1):
        reconstructed[i] = transformed_text[current_index]
        
        # Update the current index using the first column
        current_index = first_column.index(transformed_text[current_index]) + \
                        sum(next_char_map[ch] <= transformed_text[current_index] for ch in first_column[:first_column.index(transformed_text[current_index])])
    
    return ''.join(reconstructed)