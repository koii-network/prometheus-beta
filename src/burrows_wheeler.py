def burrows_wheeler_transform(input_string):
    """
    Implement the Burrows-Wheeler Transform for data compression.
    
    Args:
        input_string (str): The input string to transform.
    
    Returns:
        tuple: A tuple containing the transformed string and the original index.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Append a special terminator character that is lexicographically smaller than any other
    input_string += '$'
    
    # Generate all rotations of the input string
    rotations = [input_string[i:] + input_string[:i] for i in range(len(input_string))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Find the original index and create the transformed string
    original_index = sorted_rotations.index(input_string)
    transformed_string = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return transformed_string, original_index