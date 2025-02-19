def lzvn_compress(data):
    """
    Implement LZVN (Lempel-Ziv Variant N) compression algorithm.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    """
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        return b''
    
    compressed = bytearray()
    input_length = len(data)
    pos = 0
    
    while pos < input_length:
        # Look ahead to find the longest match
        best_length = 0
        best_offset = 0
        
        # Search back in the data for potential matches
        search_start = max(0, pos - 4096)  # Limit search window
        for search_pos in range(search_start, pos):
            match_length = 0
            
            # Check how long the match continues
            while (pos + match_length < input_length and 
                   data[search_pos + match_length] == data[pos + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = pos - search_pos
        
        # Encode the token
        if best_length > 2:
            # Compressed token: offset and length
            compressed.append(best_offset & 0xFF)  # Lower byte of offset
            compressed.append((best_offset >> 8) & 0xFF)  # Upper byte of offset
            compressed.append(best_length)
            pos += best_length
        else:
            # Literal byte
            compressed.append(data[pos])
            pos += 1
    
    return bytes(compressed)

def lzvn_decompress(compressed_data):
    """
    Decompress data compressed with LZVN algorithm.
    
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
    pos = 0
    
    while pos < len(compressed_data):
        # Check if we have a match token or a literal
        if pos + 2 < len(compressed_data):
            # Extract potential offset and length
            offset = compressed_data[pos] | (compressed_data[pos+1] << 8)
            length = compressed_data[pos+2]
            
            # Determine if this is a match token
            if offset > 0 and length > 2:
                # Expand match
                start = len(decompressed) - offset
                for _ in range(length):
                    if start < 0:
                        break
                    decompressed.append(decompressed[start])
                    start += 1
                pos += 3
            else:
                # Literal byte
                decompressed.append(compressed_data[pos])
                pos += 1
        else:
            # Remaining bytes are literals
            decompressed.append(compressed_data[pos])
            pos += 1
    
    return bytes(decompressed)