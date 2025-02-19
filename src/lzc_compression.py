def lzc_compress(input_data):
    """
    Implement LZC (Lempel-Ziv-Cleary) compression algorithm.
    
    Args:
        input_data (str or bytes): The input data to compress.
    
    Returns:
        list: A list of compressed codes representing the input data.
    
    Raises:
        TypeError: If input is not a string or bytes.
    """
    # Ensure input is bytes for consistent processing
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    elif not isinstance(input_data, bytes):
        raise TypeError("Input must be a string or bytes")
    
    # Initialize dictionary with single-character entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    result = []
    current_sequence = b''
    
    for byte in input_data:
        # Create a new sequence by adding the current byte
        test_sequence = current_sequence + bytes([byte])
        
        # If the sequence is in the dictionary, continue building
        if test_sequence in dictionary:
            current_sequence = test_sequence
        else:
            # Output the code for the current sequence
            result.append(dictionary[current_sequence])
            
            # Add the new sequence to the dictionary if not full
            if next_code < 65536:  # Limit dictionary size to 16-bit codes
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to the current byte
            current_sequence = bytes([byte])
    
    # Output the last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzc_decompress(compressed_data):
    """
    Decompress data compressed with the LZC algorithm.
    
    Args:
        compressed_data (list): List of compressed codes.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(compressed_data, list) or not all(isinstance(x, int) for x in compressed_data):
        raise TypeError("Input must be a list of integers")
    
    # Initialize dictionary with single-character entries
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Decompression variables
    result = []
    current_code = compressed_data[0]
    result.append(dictionary[current_code])
    
    for next_code_index in compressed_data[1:]:
        if next_code_index in dictionary:
            # Known code in dictionary
            decoded_sequence = dictionary[next_code_index]
        elif next_code_index == next_code:
            # Special case: new sequence not yet in dictionary
            decoded_sequence = dictionary[current_code] + bytes([dictionary[current_code][0]])
        else:
            raise ValueError(f"Invalid compressed code: {next_code_index}")
        
        result.append(decoded_sequence)
        
        # Add new sequence to dictionary if not full
        if next_code < 65536:
            dictionary[next_code] = dictionary[current_code] + bytes([decoded_sequence[0]])
            next_code += 1
        
        current_code = next_code_index
    
    return b''.join(result)