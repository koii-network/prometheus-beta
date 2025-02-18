def lzrw_compress(data):
    """
    Implement the LZRW (Lempel-Ziv Ross Williams) compression algorithm.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        return b''
    
    # Initialize compression variables
    output = bytearray()
    window_size = 4096  # Typical window size for LZRW
    look_ahead_buffer_size = 16  # Look-ahead buffer size
    
    # Position tracker
    current_pos = 0
    
    while current_pos < len(data):
        # Find the longest match in the sliding window
        best_match_length = 0
        best_match_offset = 0
        
        # Search back in the window for the longest match
        search_start = max(0, current_pos - window_size)
        for search_pos in range(search_start, current_pos):
            match_length = 0
            
            # Check how long the match continues
            while (current_pos + match_length < len(data) and 
                   match_length < look_ahead_buffer_size and 
                   data[search_pos + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if this is longer
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = current_pos - search_pos
        
        # Encode the result
        if best_match_length > 2:
            # Encode a match (offset, length)
            # Use 12 bits for offset, 4 bits for length
            match_token = ((best_match_offset & 0xFFF) << 4) | (best_match_length & 0xF)
            output.extend(match_token.to_bytes(2, byteorder='big'))
            current_pos += best_match_length
        else:
            # Encode a literal byte
            output.append(data[current_pos])
            current_pos += 1
    
    return bytes(output)

def lzrw_decompress(compressed_data):
    """
    Decompress data compressed with the LZRW algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        return b''
    
    output = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        # If not enough bytes for a full token, treat as literals
        if current_pos + 1 >= len(compressed_data):
            output.append(compressed_data[current_pos])
            break
        
        # Extract token (2 bytes)
        token = int.from_bytes(compressed_data[current_pos:current_pos+2], byteorder='big')
        
        # Decode match or literal
        offset = (token >> 4) & 0xFFF
        length = token & 0xF
        
        if length == 0:
            # Literal byte
            output.append(token & 0xFF)
            current_pos += 1
        else:
            # Back-reference match
            start = len(output) - offset
            for i in range(length):
                output.append(output[start + i])
            current_pos += 2
    
    return bytes(output)