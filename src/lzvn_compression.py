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
        # Look for the longest match
        best_length = 1
        best_offset = 0
        max_search_back = min(pos, 4096)  # Limit search window
        
        for offset in range(1, max_search_back + 1):
            match_length = 0
            
            # Check match length
            while (pos + match_length < input_length and 
                   match_length < 255 and 
                   pos - offset + match_length >= 0 and
                   data[pos - offset + match_length] == data[pos + match_length]):
                match_length += 1
            
            # Update best match if it's longer
            if match_length > best_length:
                best_length = match_length
                best_offset = offset
        
        # Encode the best match or literal
        if best_length > 2:
            # Encode match: 
            # Use two bytes for offset, one for length
            compressed.append(best_offset & 0xFF)  # Lower byte of offset
            compressed.append((best_offset >> 8) & 0x0F | 0xF0)  # Upper 4 bits of offset, top bit set
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
        # Check for match or literal
        if pos + 2 < len(compressed_data):
            # Decode offset 
            lower_offset = compressed_data[pos]
            upper_offset_flag = compressed_data[pos+1]
            length = compressed_data[pos+2]
            
            # Check if this is a match token (top 4 bits of second byte are set)
            if (upper_offset_flag & 0xF0) == 0xF0:
                # Reconstruct offset
                offset = lower_offset | ((upper_offset_flag & 0x0F) << 8)
                
                # Expand match
                start = len(decompressed) - offset
                match_start = start
                
                for _ in range(length):
                    if match_start < 0:
                        break
                    decompressed.append(decompressed[match_start])
                    match_start += 1
                
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