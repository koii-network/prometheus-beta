def lzvn_compress(data):
    """
    Implement a basic LZVN (Lempel-Ziv Variant N) compression algorithm.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    """
    # Initialize compression parameters
    compressed = bytearray()
    window_size = 4096  # Typical sliding window size
    max_match_length = 255  # Maximum match length
    
    # Current position in the input data
    current_pos = 0
    
    while current_pos < len(data):
        # Look for the longest match in the previous window
        best_match_length = 0
        best_match_offset = 0
        
        # Search back in the window
        search_start = max(0, current_pos - window_size)
        for offset in range(search_start, current_pos):
            match_length = 0
            
            # Check how long the match continues
            while (current_pos + match_length < len(data) and 
                   match_length < max_match_length and 
                   data[offset + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = current_pos - offset
        
        # Encode the result
        if best_match_length > 2:  # Compression is beneficial
            # Encode match: [offset, length]
            compressed.extend([
                (best_match_offset >> 8) & 0xFF,  # High byte of offset
                best_match_offset & 0xFF,         # Low byte of offset
                best_match_length                 # Match length
            ])
            current_pos += best_match_length
        else:
            # Literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return bytes(compressed)

def lzvn_decompress(compressed_data):
    """
    Decompress data compressed with the LZVN algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed original data
    """
    decompressed = bytearray()
    pos = 0
    
    while pos < len(compressed_data):
        # Check if it's a match or a literal
        if pos + 2 < len(compressed_data):
            # Potential match
            offset = (compressed_data[pos] << 8) | compressed_data[pos + 1]
            length = compressed_data[pos + 2]
            
            # If it looks like a valid match
            if length > 0:
                # Calculate start position in decompressed data
                match_start = len(decompressed) - offset
                
                # Copy matched sequence
                for i in range(length):
                    if match_start + i >= 0:
                        decompressed.append(decompressed[match_start + i])
                
                pos += 3  # Move past match header
                continue
        
        # Literal byte
        decompressed.append(compressed_data[pos])
        pos += 1
    
    return bytes(decompressed)