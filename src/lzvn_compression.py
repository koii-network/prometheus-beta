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
    window_size = 256  # Small window for demonstration
    
    # Current position in the input data
    pos = 0
    
    while pos < len(data):
        # Look for the longest match in the current window
        best_match_length = 0
        best_match_offset = 0
        
        # Search back in the current window
        window_start = max(0, pos - window_size)
        for offset in range(window_start, pos):
            match_length = 0
            
            # Check how long the match continues
            while (pos + match_length < len(data) and 
                   data[offset + match_length] == data[pos + match_length] and 
                   match_length < 15):  # Limit match length
                match_length += 1
            
            # Update best match if current is longer
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = pos - offset
        
        # Encode the token
        if best_match_length >= 3:
            # Compressed token: [offset:4 bits][length:4 bits]
            token = ((best_match_offset & 0x0F) << 4) | (best_match_length & 0x0F)
            compressed.append(token)
            pos += best_match_length
        else:
            # Literal byte
            compressed.append(data[pos])
            pos += 1
    
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
    pos = 0
    
    while pos < len(compressed_data):
        # Check if it's a compressed token or a literal
        current_byte = compressed_data[pos]
        
        # Token: high 4 bits are offset, low 4 bits are length
        if current_byte >> 4 != 0 or current_byte & 0x0F != 0:
            offset = (current_byte >> 4) & 0x0F
            length = current_byte & 0x0F
            
            # Reconstruct offset from the token
            match_start = len(decompressed) - offset
            
            # Copy matched sequence
            for i in range(length):
                decompressed.append(decompressed[match_start + i])
            
            pos += 1
        else:
            # Literal byte
            decompressed.append(current_byte)
            pos += 1
    
    return bytes(decompressed)