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
    
    # LZJB compression parameters
    NBBY = 8  # Number of bits in a byte
    MATCH_BITS = 6
    MATCH_MAX = (1 << MATCH_BITS) - 1
    OFFSET_MASK = (1 << (16 - MATCH_BITS)) - 1
    
    # Compression output
    compressed = bytearray()
    
    # Compression state
    src_len = len(input_data)
    src_idx = 0
    dst_idx = 0
    
    while src_idx < src_len:
        # Look back for potential matches
        hash_match_len = 0
        hash_match_offset = 0
        
        # Look back up to 1024 bytes (typical LZJB window)
        look_back = min(src_idx, 1024)
        
        for offset in range(1, look_back + 1):
            match_len = 0
            
            # Check how long the match can be
            while (src_idx + match_len < src_len and 
                   match_len < MATCH_MAX and 
                   input_data[src_idx - offset + match_len] == input_data[src_idx + match_len]):
                match_len += 1
            
            # Update best match if found
            if match_len > hash_match_len:
                hash_match_len = match_len
                hash_match_offset = offset
        
        # Encode match or literal
        if hash_match_len > 2:
            # Encode match
            match_token = ((hash_match_offset - 1) << MATCH_BITS) | (hash_match_len - 3)
            compressed.append(match_token)
            src_idx += hash_match_len
        else:
            # Encode literal
            compressed.append(input_data[src_idx])
            src_idx += 1
    
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
    
    # LZJB compression parameters
    NBBY = 8  # Number of bits in a byte
    MATCH_BITS = 6
    MATCH_MAX = (1 << MATCH_BITS) - 1
    OFFSET_MASK = (1 << (16 - MATCH_BITS)) - 1
    
    # Decompression state
    decompressed = bytearray()
    src_idx = 0
    
    while src_idx < len(compressed_data):
        token = compressed_data[src_idx]
        src_idx += 1
        
        # Check if this is a match or a literal
        if token >= (1 << MATCH_BITS):
            # This is a match
            match_offset = (token >> MATCH_BITS) + 1
            match_len = (token & MATCH_MAX) + 3
            
            # Reconstruct match data from previous decompressed data
            start_idx = len(decompressed) - match_offset
            
            for _ in range(match_len):
                decompressed.append(decompressed[start_idx])
                start_idx += 1
        else:
            # This is a literal
            decompressed.append(token)
    
    return bytes(decompressed)