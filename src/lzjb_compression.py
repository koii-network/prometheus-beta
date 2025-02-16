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
        return b''
    
    compressed = bytearray()
    input_length = len(input_data)
    
    # Compression parameters
    MATCH_BITS = 6
    MATCH_MIN = 3
    MATCH_MAX = (1 << MATCH_BITS) + (MATCH_MIN - 1)
    WINDOW_SIZE = 1024  # Reduced window size for stability
    
    src_pos = 0
    while src_pos < input_length:
        # Look for a match in the window
        match_found = False
        match_offset = 0
        match_length = 0
        
        # Search back in the window for a match
        search_back = min(src_pos, WINDOW_SIZE)
        for back_dist in range(1, search_back + 1):
            potential_match_length = 0
            
            # Check for match length
            while (potential_match_length < MATCH_MAX and 
                   src_pos + potential_match_length < input_length and 
                   src_pos - back_dist + potential_match_length >= 0 and
                   input_data[src_pos - back_dist + potential_match_length] == 
                   input_data[src_pos + potential_match_length]):
                potential_match_length += 1
            
            # If a match is found and long enough
            if potential_match_length >= MATCH_MIN:
                match_found = True
                match_offset = back_dist
                match_length = potential_match_length
                break
        
        # Encode either a literal or a match
        if not match_found or match_length < MATCH_MIN:
            # Literal byte
            compressed.append(input_data[src_pos])
            src_pos += 1
        else:
            # Encode match with offset and length
            # Ensure match_code is within byte range (0-255)
            match_offset_bits = min(((match_offset - 1) << MATCH_BITS) & 0xFF, 255)
            match_length_bits = min((match_length - MATCH_MIN) & ((1 << MATCH_BITS) - 1), 63)
            match_code = match_offset_bits | (match_length_bits | 0x80)  # Set high bit for match
            
            compressed.append(match_code)
            src_pos += match_length
    
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
        return b''
    
    # Decompression parameters
    MATCH_BITS = 6
    MATCH_MIN = 3
    
    decompressed = bytearray()
    src_pos = 0
    
    while src_pos < len(compressed_data):
        current_byte = compressed_data[src_pos]
        
        # Check if it's a match or a literal
        if current_byte < 128:  # Literal byte
            decompressed.append(current_byte)
            src_pos += 1
        else:
            # Decode match
            match_code = current_byte
            match_offset = ((match_code >> MATCH_BITS) & 0x1F) + 1
            match_length = (match_code & ((1 << MATCH_BITS) - 1)) + MATCH_MIN
            
            # Perform match copy
            start_pos = len(decompressed) - match_offset
            for i in range(match_length):
                # Add some safety checks
                if start_pos + i < 0 or start_pos + i >= len(decompressed):
                    break
                decompressed.append(decompressed[start_pos + i])
            
            src_pos += 1
    
    return bytes(decompressed)