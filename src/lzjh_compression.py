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
            compressed.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not at max limit
            if next_code < 65536:  # Limit dictionary size
                dictionary[potential_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Output last sequence
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    # Convert to bytes
    return bytes(compressed)

def lzjh_decompress(compressed_data):
    """
    Decompress data compressed with LZJH algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    # Initialize decompression dictionary
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Convert compressed data to list if it's bytes
    if isinstance(compressed_data, bytes):
        compressed_data = list(compressed_data)
    
    # First code is always output directly
    result = [compressed_data[0]]
    previous = dictionary[compressed_data[0]]
    
    # Decompression logic
    for code in compressed_data[1:]:
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