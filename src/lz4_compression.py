def lz4_compress(data):
    """
    Implement a simplified LZ4 compression algorithm.
    
    Args:
        data (bytes or str): Input data to compress
    
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
    
    # Compressed data will store: 
    # 1. Compressed tokens
    # 2. Literal sequences
    compressed = bytearray()
    
    # Index to track current position in the input data
    i = 0
    
    while i < len(data):
        # Look for repeated sequences
        best_match_length = 0
        best_match_offset = 0
        
        # Search back in the data for repeated sequences
        for j in range(max(0, i - 65535), i):
            # Calculate potential match length
            match_length = 0
            while (i + match_length < len(data) and 
                   data[i + match_length] == data[j + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # Update best match if found
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = i - j
        
        # If a good match is found
        if best_match_length >= 4:
            # Encode match token
            # First byte: match length (capped at 15)
            # Second byte: offset
            match_token = min(best_match_length, 15)
            compressed.append(match_token << 4 | (min(best_match_offset, 15)))
            
            if best_match_length >= 15:
                compressed.append(best_match_length - 15)
            
            compressed.extend(data[i + best_match_length:i + best_match_length + best_match_offset])
            
            i += best_match_length
        else:
            # Literal sequence
            compressed.append(1)  # Literal sequence token
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lz4_decompress(compressed_data):
    """
    Decompress LZ4 compressed data.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Extract token
        token = compressed_data[i]
        match_length = token >> 4
        literal_length = token & 0x0F
        
        i += 1
        
        # Handle extended match length
        if match_length == 15:
            while compressed_data[i] == 255:
                match_length += 255
                i += 1
            match_length += compressed_data[i]
            i += 1
        
        # Copy match
        if match_length > 0:
            decompressed.extend(decompressed[-match_length:])
        
        # End of stream
        if i >= len(compressed_data):
            break
        
        # Add literals
        for _ in range(literal_length):
            decompressed.append(compressed_data[i])
            i += 1
    
    return bytes(decompressed)