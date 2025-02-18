def lz4_compress(data):
    """
    Implement a basic LZ4 compression algorithm.
    
    LZ4 is a fast lossless compression algorithm that focuses on compression and 
    decompression speed rather than compression ratio.
    
    Args:
        data (bytes or str): The input data to compress
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
    """
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Basic LZ4-like compression using dictionary-based approach
    compressed = bytearray()
    dictionary = {}
    current_sequence = bytearray()
    
    for byte in data:
        # Try to extend current sequence
        test_sequence = current_sequence + bytes([byte])
        
        if bytes(test_sequence) in dictionary:
            # If sequence exists in dictionary, continue building it
            current_sequence = test_sequence
        else:
            # When sequence is not in dictionary
            if current_sequence:
                # Encode the previous sequence
                if bytes(current_sequence) in dictionary:
                    # Use dictionary reference
                    compressed.extend([dictionary[bytes(current_sequence)]])
                else:
                    # Literal byte encoding
                    for b in current_sequence:
                        compressed.extend([0, b])  # 0 indicates literal byte
                
                # Add new sequence to dictionary
                dictionary[bytes(test_sequence)] = len(dictionary)
            
            # Reset current sequence to new byte
            current_sequence = bytearray([byte])
    
    # Handle remaining sequence
    if current_sequence:
        if bytes(current_sequence) in dictionary:
            compressed.extend([dictionary[bytes(current_sequence)]])
        else:
            for b in current_sequence:
                compressed.extend([0, b])
    
    return bytes(compressed)

def lz4_decompress(compressed_data):
    """
    Decompress LZ4-like compressed data.
    
    Args:
        compressed_data (bytes): The compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompression dictionary and output
    dictionary = {}
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        if compressed_data[i] == 0:
            # Literal byte
            if i + 1 >= len(compressed_data):
                break
            literal = compressed_data[i + 1]
            decompressed.append(literal)
            
            # Update dictionary
            if len(decompressed) > 1:
                dictionary[len(dictionary)] = bytes(decompressed[-2:])
            
            i += 2
        else:
            # Dictionary reference
            ref = compressed_data[i]
            if ref < len(dictionary):
                sequence = dictionary[ref]
                decompressed.extend(sequence)
                
                # Update dictionary
                if len(decompressed) > 1:
                    dictionary[len(dictionary)] = bytes(decompressed[-2:])
            else:
                # Invalid reference
                raise ValueError("Invalid compression dictionary reference")
            
            i += 1
    
    return bytes(decompressed)