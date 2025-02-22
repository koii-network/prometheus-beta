def lzvn_compress(data):
    """
    Implement a basic LZVN-like compression algorithm.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        return b''
    
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Look-ahead buffer for finding repeating sequences
        match_length = 0
        match_offset = 0
        
        # Search back for the longest matching sequence
        for back_offset in range(1, min(i + 1, 4096)):  # Limit search to reasonable window
            # Check potential match length
            current_match_length = 0
            while (i + current_match_length < len(data) and 
                   current_match_length < 15 and  # Limit match length to 4 bits
                   data[i + current_match_length] == data[i - back_offset + current_match_length]):
                current_match_length += 1
            
            # Update best match if found
            if current_match_length > match_length:
                match_length = current_match_length
                match_offset = back_offset
        
        # Encode the result
        if match_length >= 3:  # Minimum meaningful match
            # Compression: offset and length
            compressed.append((match_offset & 0x0F) << 4 | (match_length & 0x0F))
            i += match_length
        else:
            # No compression: literal byte
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lzvn_decompress(compressed_data):
    """
    Decompress data compressed with the LZVN-like algorithm.
    
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
        # Get current byte
        current_byte = compressed_data[i]
        
        # Check if it's a compression token or literal
        if current_byte >> 4 > 0:  # Compression token
            # Extract offset and length
            match_offset = current_byte >> 4
            match_length = current_byte & 0x0F
            
            # Copy matched sequence
            start_pos = len(decompressed) - match_offset
            for j in range(match_length):
                decompressed.append(decompressed[start_pos + j])
        else:
            # Literal byte
            decompressed.append(current_byte)
        
        i += 1
    
    return bytes(decompressed)