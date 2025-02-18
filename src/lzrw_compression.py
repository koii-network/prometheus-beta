def lzrw_compress(input_data):
    """
    Implement the LZRW (Lempel-Ziv Ross Williams) compression algorithm.
    
    Args:
        input_data (bytes or str): The data to be compressed.
    
    Returns:
        bytes: Compressed data.
    """
    # Ensure input is bytes
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Initialize compression parameters
    compressed = bytearray()
    window_size = 4096  # Typical window size for LZRW
    lookahead_size = 16  # Maximum match length
    
    # Initialize sliding window and current position
    current_pos = 0
    
    while current_pos < len(input_data):
        # Find the longest match in the previous window
        best_match_length = 0
        best_match_offset = 0
        
        # Search back in the window for the longest match
        search_start = max(0, current_pos - window_size)
        for search_pos in range(search_start, current_pos):
            match_length = 0
            
            # Check how long the match continues
            while (match_length < lookahead_size and 
                   current_pos + match_length < len(input_data) and 
                   input_data[search_pos + match_length] == input_data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = current_pos - search_pos
        
        # Encode the result
        if best_match_length > 2:
            # Encode a match (offset, length)
            compressed.append(0x80 | ((best_match_offset >> 8) & 0x0F))
            compressed.append(best_match_offset & 0xFF)
            compressed.append(best_match_length - 3)
            current_pos += best_match_length
        else:
            # Encode a literal byte
            compressed.append(input_data[current_pos])
            current_pos += 1
    
    return bytes(compressed)

def lzrw_decompress(compressed_data):
    """
    Decompress data compressed with the LZRW algorithm.
    
    Args:
        compressed_data (bytes): The data to be decompressed.
    
    Returns:
        bytes: Decompressed data.
    """
    # Ensure input is bytes
    if isinstance(compressed_data, str):
        compressed_data = compressed_data.encode('utf-8')
    
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        # Check if it's a match or a literal
        flag = compressed_data[current_pos]
        
        if flag & 0x80:
            # Match encoding
            offset = ((flag & 0x0F) << 8) | compressed_data[current_pos + 1]
            length = compressed_data[current_pos + 2] + 3
            
            # Calculate source position for copy
            source_pos = len(decompressed) - offset
            
            # Copy matched bytes
            for _ in range(length):
                decompressed.append(decompressed[source_pos])
                source_pos += 1
            
            current_pos += 3
        else:
            # Literal byte
            decompressed.append(flag)
            current_pos += 1
    
    return bytes(decompressed)