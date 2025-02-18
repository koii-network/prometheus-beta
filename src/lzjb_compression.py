def lzjb_compress(input_data):
    """
    Implement LZJB compression algorithm.
    
    Args:
        input_data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not input_data:
        return bytes()
    
    # LZJB parameters
    BITS = 8  # Bit width for offset and length
    MAX_OFFSET = (1 << BITS) - 1
    MAX_LENGTH = (1 << BITS) - 1
    
    compressed = bytearray()
    input_length = len(input_data)
    current_pos = 0
    
    while current_pos < input_length:
        # Try to find the best match in the previous window
        best_length = 0
        best_offset = 0
        
        # Look back up to MAX_OFFSET bytes
        lookback_start = max(0, current_pos - MAX_OFFSET)
        lookback_end = current_pos
        
        for offset in range(lookback_start, lookback_end):
            match_length = 0
            
            # Check match length
            while (current_pos + match_length < input_length and 
                   input_data[current_pos + match_length] == input_data[offset + match_length] and 
                   match_length < MAX_LENGTH):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = current_pos - offset
        
        # Encode match or literal
        if best_length > 0:
            # Compressed token: high 8 bits are offset, low 8 bits are length
            token = ((best_offset & 0xFF) << BITS) | (best_length & 0xFF)
            compressed.append(token)
            current_pos += best_length
        else:
            # Literal byte
            compressed.append(input_data[current_pos])
            current_pos += 1
    
    return bytes(compressed)

def lzjb_decompress(compressed_data):
    """
    Implement LZJB decompression algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        return bytes()
    
    # LZJB parameters
    BITS = 8  # Bit width for offset and length
    
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        token = compressed_data[current_pos]
        current_pos += 1
        
        # Check if it's a literal or a match
        if token < 256:
            # Literal byte
            decompressed.append(token)
        else:
            # Compressed token
            offset = token >> BITS
            length = token & 0xFF
            
            # Reconstruct match
            match_start = len(decompressed) - offset
            for i in range(length):
                decompressed.append(decompressed[match_start + i])
    
    return bytes(decompressed)