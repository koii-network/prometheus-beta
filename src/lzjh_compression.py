def lzjh_compress(data):
    """
    Implement the LZJH (Lempel-Ziv-Jenkins-Huffman) compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
    """
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # If input is empty, return empty bytes
    if not data:
        return b''
    
    # Initialize dictionary and compression variables
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    compressed = []
    current_sequence = b''
    
    for byte in data:
        # Extend current sequence
        current_sequence += bytes([byte])
        
        # If current sequence is not in dictionary, add it
        if current_sequence not in dictionary:
            # Output code for previous sequence
            compressed.append(dictionary[current_sequence[:-1]])
            
            # Add new sequence to dictionary if space allows
            if next_code < 65536:  # Limit dictionary size to 16-bit codes
                dictionary[current_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to last byte
            current_sequence = bytes([byte])
    
    # Output code for final sequence
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    # Convert to bytes representation
    return bytes(compressed)

def lzjh_decompress(compressed_data):
    """
    Decompress data compressed with the LZJH algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not compressed_data:
        return b''
    
    # Initialize dictionary and decompression variables
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    result = []
    
    # First code is always processed directly
    current_code = compressed_data[0]
    result.append(dictionary[current_code])
    previous_sequence = dictionary[current_code]
    
    # Process remaining codes
    for code in compressed_data[1:]:
        sequence = dictionary.get(code)
        
        if sequence is None:
            # Special case: new sequence not yet in dictionary
            sequence = previous_sequence + bytes([previous_sequence[0]])
        
        result.append(sequence)
        
        # Add new dictionary entry
        if next_code < 65536:  # Limit dictionary size to 16-bit codes
            dictionary[next_code] = previous_sequence + bytes([sequence[0]])
            next_code += 1
        
        previous_sequence = sequence
    
    return b''.join(result)