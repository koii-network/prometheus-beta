def lzjb_compress(input_data):
    """
    Implement the LZJB compression algorithm.
    
    Args:
        input_data (bytes): The input data to compress
    
    Returns:
        bytes: Compressed data
    """
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes")
    
    compressed = bytearray()
    input_length = len(input_data)
    
    # Sliding window parameters
    WINDOW_SIZE = 1024
    MATCH_BITS = 6
    MATCH_MIN = 3
    OFFSET_MASK = (1 << (16 - MATCH_BITS)) - 1
    
    current_pos = 0
    while current_pos < input_length:
        # Find the best match in the sliding window
        best_match_len = 0
        best_match_offset = 0
        
        # Look back in the window to find the longest match
        window_start = max(0, current_pos - WINDOW_SIZE)
        for look_back_pos in range(window_start, current_pos):
            match_len = 0
            
            # Check how long the match is
            while (current_pos + match_len < input_length and 
                   input_data[look_back_pos + match_len] == input_data[current_pos + match_len] and 
                   match_len < (1 << MATCH_BITS) - 1):
                match_len += 1
            
            # Update best match if this is longer
            if match_len >= MATCH_MIN and match_len > best_match_len:
                best_match_len = match_len
                best_match_offset = current_pos - look_back_pos
        
        # Encoding logic
        if best_match_len >= MATCH_MIN:
            # Encode match as (offset, length)
            encoded = ((best_match_offset & OFFSET_MASK) << MATCH_BITS) | (best_match_len - MATCH_MIN)
            compressed.append((encoded >> 8) & 0xFF)  # High byte
            compressed.append(encoded & 0xFF)         # Low byte
            current_pos += best_match_len
        else:
            # Literal byte
            compressed.append(input_data[current_pos])
            current_pos += 1
    
    return bytes(compressed)

def lzjb_decompress(compressed_data):
    """
    Decompress data compressed with the LZJB algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    decompressed = bytearray()
    input_length = len(compressed_data)
    
    # Sliding window parameters
    MATCH_BITS = 6
    MATCH_MIN = 3
    OFFSET_MASK = (1 << (16 - MATCH_BITS)) - 1
    
    current_pos = 0
    while current_pos < input_length:
        # Decode the current token
        if current_pos + 1 >= input_length:
            # Literal byte at the end
            decompressed.append(compressed_data[current_pos])
            break
        
        # Reconstruct the encoded token
        token = (compressed_data[current_pos] << 8) | compressed_data[current_pos + 1]
        
        # Check if it's a match or literal
        offset = (token >> MATCH_BITS) & OFFSET_MASK
        length = (token & ((1 << MATCH_BITS) - 1)) + MATCH_MIN
        
        if offset == 0 and length == MATCH_MIN - 1:
            # Literal byte
            decompressed.append(compressed_data[current_pos])
            current_pos += 1
        else:
            # Match: copy from previous data
            match_start = len(decompressed) - offset
            for i in range(length):
                decompressed.append(decompressed[match_start + i])
            current_pos += 2
    
    return bytes(decompressed)