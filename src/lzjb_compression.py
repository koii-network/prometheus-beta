def lzjb_compress(data):
    """
    Implement LZJB compression algorithm.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    # Compression parameters
    NBBY = 8  # Number of bits in a byte
    MATCH_BITS = 6
    MATCH_MIN = 3
    MATCH_MAX = (1 << MATCH_BITS) + (MATCH_MIN - 1)
    OFFSET_MASK = (1 << (16 - MATCH_BITS)) - 1

    # Output buffer and current position
    compressed = bytearray()
    src_pos = 0
    src_len = len(data)

    while src_pos < src_len:
        # Look-ahead window
        look_ahead = min(src_len - src_pos, MATCH_MAX)
        
        # Find best match in previous window
        best_len = 0
        best_offset = 0
        
        if look_ahead >= MATCH_MIN:
            # Search back in previous data
            search_start = max(0, src_pos - OFFSET_MASK)
            for back_pos in range(src_pos - 1, search_start - 1, -1):
                current_len = 0
                
                # Check match length
                while (current_len < look_ahead and 
                       src_pos + current_len < src_len and 
                       data[back_pos + current_len] == data[src_pos + current_len]):
                    current_len += 1
                
                # Update best match if longer
                if current_len > best_len:
                    best_len = current_len
                    best_offset = src_pos - back_pos
        
        # Compression decision
        if best_len >= MATCH_MIN:
            # Encode match
            token = ((best_offset << MATCH_BITS) | (best_len - MATCH_MIN)) & 0xFF
            compressed.append(token)
            src_pos += best_len
        else:
            # Encode literal
            compressed.append(data[src_pos])
            src_pos += 1
    
    return bytes(compressed)

def lzjb_decompress(compressed_data):
    """
    Implement LZJB decompression algorithm.
    
    Args:
        compressed_data (bytes): Input compressed data
    
    Returns:
        bytes: Decompressed data
    """
    # Compression parameters
    MATCH_BITS = 6
    MATCH_MIN = 3
    MATCH_MAX = (1 << MATCH_BITS) + (MATCH_MIN - 1)
    OFFSET_MASK = (1 << (16 - MATCH_BITS)) - 1

    # Output buffer and current positions
    decompressed = bytearray()
    src_pos = 0
    src_len = len(compressed_data)

    while src_pos < src_len:
        token = compressed_data[src_pos]
        src_pos += 1

        if token < (1 << MATCH_BITS):
            # Literal byte
            decompressed.append(token)
        else:
            # Compressed token
            match_len = (token & ((1 << MATCH_BITS) - 1)) + MATCH_MIN
            match_offset = token >> MATCH_BITS
            
            # Reconstruct match from previous data
            start = len(decompressed) - match_offset
            for i in range(match_len):
                decompressed.append(decompressed[start + i])
    
    return bytes(decompressed)