def lzc_compress(input_data):
    """
    Implement Lempel-Ziv-Childers (LZC) compression algorithm.
    
    Args:
        input_data (bytes or str): The input data to compress.
    
    Returns:
        list: Compressed data as a list of integer codes.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Convert input to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate input
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or str")
    
    if not input_data:
        raise ValueError("Input cannot be empty")
    
    # Initialize dictionary and compression variables
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    max_dict_size = 65536  # Limit dictionary size to 16-bit codes
    
    # Compression variables
    current_sequence = bytes([input_data[0]])
    compressed_output = []
    
    # Compression algorithm
    for byte in input_data[1:]:
        # Try to extend the current sequence
        test_sequence = current_sequence + bytes([byte])
        
        if test_sequence in dictionary:
            # If sequence exists, keep extending
            current_sequence = test_sequence
        else:
            # Output the code for current sequence
            compressed_output.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not full
            if next_code < max_dict_size:
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Output last sequence
    compressed_output.append(dictionary[current_sequence])
    
    return compressed_output