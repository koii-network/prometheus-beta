def lzc_compress(input_data):
    """
    Implement Lempel-Ziv-Cleary (LZC) compression algorithm.
    
    Args:
        input_data (str or bytes): The input data to compress.
    
    Returns:
        list: Compressed data represented as a list of integer codes.
    
    Raises:
        TypeError: If input is not a string or bytes.
    """
    # Ensure input is bytes
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    elif not isinstance(input_data, bytes):
        raise TypeError("Input must be a string or bytes")
    
    # Initialize dictionary with single-character entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    max_dict_size = 65536  # Limit dictionary size to prevent excessive memory usage
    
    # Initialize compression variables
    compressed = []
    current_sequence = b''
    
    for byte in input_data:
        # Try to extend the current sequence
        test_sequence = current_sequence + bytes([byte])
        
        if test_sequence in dictionary:
            # If sequence exists, continue building it
            current_sequence = test_sequence
        else:
            # Output the code for the current sequence
            compressed.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not at max size
            if next_code < max_dict_size:
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to current byte
            current_sequence = bytes([byte])
    
    # Output the last sequence
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    return compressed