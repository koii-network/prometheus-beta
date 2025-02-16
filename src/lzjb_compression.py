def lzjb_compress(input_data):
    """
    Implement a simplified LZJB-like compression algorithm.
    
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
    window_size = 1024  # Sliding window size
    
    src_pos = 0
    while src_pos < input_length:
        # Search back in the window for the longest match
        max_match_length = 0
        max_match_offset = 0
        search_start = max(0, src_pos - window_size)
        
        for back_dist in range(1, src_pos - search_start + 1):
            match_length = 0
            while (src_pos + match_length < input_length and
                   src_pos - back_dist + match_length >= search_start and
                   input_data[src_pos + match_length] == 
                   input_data[src_pos - back_dist + match_length] and
                   match_length < 63):  # max match length is 63
                match_length += 1
            
            if match_length > max_match_length:
                max_match_length = match_length
                max_match_offset = back_dist
        
        # Decide whether to output a literal or a match
        if max_match_length < 3:  # Not worth encoding a match
            compressed.append(input_data[src_pos])
            src_pos += 1
        else:
            # Encode match: combine offset and length
            # High bit marks this as a match
            match_code = 0x80 | ((max_match_offset - 1) << 3) | (max_match_length - 3)
            compressed.append(match_code)
            src_pos += max_match_length
    
    return bytes(compressed)

def lzjb_decompress(compressed_data):
    """
    Implement a corresponding decompression algorithm.
    
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
    src_pos = 0
    
    while src_pos < len(compressed_data):
        current_byte = compressed_data[src_pos]
        
        # Check if it's a literal or a match
        if current_byte < 0x80:  # Literal
            decompressed.append(current_byte)
            src_pos += 1
        else:
            # Decode match
            offset = ((current_byte >> 3) & 0x0F) + 1
            length = (current_byte & 0x07) + 3
            
            # Copy from previous part of output
            start_pos = len(decompressed) - offset
            for _ in range(length):
                decompressed.append(decompressed[start_pos])
                start_pos += 1
            
            src_pos += 1
    
    return bytes(decompressed)