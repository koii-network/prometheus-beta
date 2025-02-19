def lzjh_compress(data):
    """
    Implement LZJH (Lempel-Ziv-Jenkins-Huffman) compression algorithm.
    
    Args:
        data (bytes or str): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    """
    # Ensure input is in bytes
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Empty input case
    if not data:
        return bytes()
    
    # Initialize compression dictionary and output
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    current_sequence = bytes()
    compressed = []
    
    # Compression logic
    for byte in data:
        # Extend current sequence
        potential_sequence = current_sequence + bytes([byte])
        
        # If sequence exists in dictionary, update current sequence
        if potential_sequence in dictionary:
            current_sequence = potential_sequence
        else:
            # Output code for current sequence
            code = dictionary[current_sequence]
            compressed.append(code)
            
            # Add new sequence to dictionary if not at max limit
            if next_code < 65536:  # Limit dictionary size
                dictionary[potential_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Output last sequence
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    # Convert to 2-byte big-endian codes
    result = bytearray()
    for code in compressed:
        result.extend(code.to_bytes(2, byteorder='big'))
    
    return bytes(result)

def lzjh_decompress(compressed_data):
    """
    Decompress data compressed with LZJH algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    # Empty input case
    if not compressed_data:
        return bytes()
    
    # Decode 2-byte codes
    compressed_codes = [int.from_bytes(compressed_data[i:i+2], byteorder='big')
                        for i in range(0, len(compressed_data), 2)]
    
    # Initialize decompression dictionary
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # First code
    result = list(dictionary[compressed_codes[0]])
    previous = dictionary[compressed_codes[0]]
    
    # Decompression logic
    for code in compressed_codes[1:]:
        # Determine current sequence
        if code in dictionary:
            current = dictionary[code]
        elif code == next_code:
            current = previous + previous[:1]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        # Output current sequence
        result.extend(current)
        
        # Add new dictionary entry if not at max limit
        if next_code < 65536:
            dictionary[next_code] = previous + current[:1]
            next_code += 1
        
        # Update previous sequence
        previous = current
    
    return bytes(result)