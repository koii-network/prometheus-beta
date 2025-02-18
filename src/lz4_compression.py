def lz4_compress(data):
    """
    Implement a basic LZ4 compression algorithm.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    # Basic LZ4-inspired compression algorithm
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        return b''
    
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Look for repeating sequences
        literal_start = i
        literal_length = 0
        match_found = False
        
        # Find potential match
        for match_length in range(4, min(65535, len(data) - i)):
            # Look back for matching sequence
            for back_distance in range(1, min(65535, i + 1)):
                if data[i:i+match_length] == data[i-back_distance:i-back_distance+match_length]:
                    # Match found
                    compressed.extend([literal_length])  # Literal length
                    compressed.extend(data[literal_start:i])  # Literals
                    
                    # Encode match length and back distance
                    compressed.extend([match_length & 0xFF, match_length >> 8])
                    compressed.extend([back_distance & 0xFF, back_distance >> 8])
                    
                    i += match_length
                    match_found = True
                    break
            
            if match_found:
                break
        
        # If no match found, add as literal
        if not match_found:
            literal_length += 1
            i += 1
            
            # If literal sequence gets too long, flush
            if literal_length == 255:
                compressed.extend([255])
                compressed.extend(data[literal_start:i])
                literal_start = i
                literal_length = 0
    
    # Flush remaining literals
    if literal_length > 0:
        compressed.extend([literal_length])
        compressed.extend(data[literal_start:i])
    
    return bytes(compressed)

def lz4_decompress(compressed_data):
    """
    Decompress data compressed with the lz4_compress function.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        return b''
    
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Read literal length
        literal_length = compressed_data[i]
        i += 1
        
        # Copy literals
        if literal_length > 0:
            decompressed.extend(compressed_data[i:i+literal_length])
            i += literal_length
        
        # Check if we've reached the end
        if i >= len(compressed_data):
            break
        
        # Read match length
        match_length = compressed_data[i] | (compressed_data[i+1] << 8)
        i += 2
        
        # Read back distance
        back_distance = compressed_data[i] | (compressed_data[i+1] << 8)
        i += 2
        
        # Copy match
        match_start = len(decompressed) - back_distance
        for j in range(match_length):
            decompressed.append(decompressed[match_start + j])
    
    return bytes(decompressed)