def lz4_compress(data):
    """
    Implement a basic LZ4 compression algorithm.
    
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
    
    compressed = bytearray()
    pos = 0
    
    while pos < len(data):
        # Look for repeating sequences
        max_match_length = 0
        match_offset = 0
        
        # Search back up to 65535 bytes
        look_back = min(pos, 65535)
        
        for offset in range(1, look_back + 1):
            current_match_length = 0
            
            # Check how long the repeating sequence is
            while (pos + current_match_length < len(data) and 
                   pos - offset + current_match_length >= 0 and 
                   current_match_length < 255 and 
                   data[pos + current_match_length] == data[pos - offset + current_match_length]):
                current_match_length += 1
            
            # Update best match
            if current_match_length > max_match_length:
                max_match_length = current_match_length
                match_offset = offset
        
        # Encode token
        if max_match_length > 4:
            # Compressed token
            # High byte of offset, low byte of offset, match length
            compressed.extend([
                (match_offset >> 8) & 0xFF,  # High byte of offset
                match_offset & 0xFF,         # Low byte of offset
                max_match_length             # Match length
            ])
            pos += max_match_length
        else:
            # Literal byte
            compressed.extend([0, data[pos]])
            pos += 1
    
    # Add end marker
    compressed.extend([0xFF, 0xFF, 0x00])
    
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
    
    decompressed = bytearray()
    pos = 0
    
    while pos < len(compressed_data) - 2:
        # Check for end marker
        if (compressed_data[pos] == 0xFF and 
            compressed_data[pos+1] == 0xFF and 
            compressed_data[pos+2] == 0x00):
            break
        
        if compressed_data[pos] == 0:
            # Literal byte
            if pos + 1 >= len(compressed_data):
                break
            
            decompressed.append(compressed_data[pos + 1])
            pos += 2
        else:
            # Compressed token
            if pos + 2 >= len(compressed_data):
                break
            
            # Reconstruct offset and match length
            offset_high = compressed_data[pos]
            offset_low = compressed_data[pos + 1]
            match_length = compressed_data[pos + 2]
            
            # Reconstruct full offset
            offset = (offset_high << 8) | offset_low
            
            # Make sure we have enough data to copy from
            if offset > len(decompressed):
                # Note: This prevents index out of range, but may not fully reproduce original
                break
            
            # Copy matched sequence from decompressed
            start = len(decompressed) - offset
            for _ in range(match_length):
                if start < 0:
                    break
                decompressed.append(decompressed[start])
                start += 1
            
            pos += 3
    
    return bytes(decompressed)