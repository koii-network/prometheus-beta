def lzrw_compress(data):
    """
    Implement simplified LZRW compression algorithm.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    if not data:
        return b''
    
    MAX_WINDOW = 4096
    compressed = bytearray()
    window = bytearray()
    input_pos = 0
    
    while input_pos < len(data):
        best_match_length = 0
        best_match_offset = 0
        
        # Find best match in current window
        for offset in range(1, min(len(window) + 1, MAX_WINDOW)):
            # Only look for match if enough data exists
            if len(window) < offset:
                continue
            
            match_start = len(window) - offset
            match_length = 0
            
            # Check for matching sequence
            while (match_length < 255 and 
                   input_pos + match_length < len(data) and 
                   match_start + match_length < len(window) and
                   window[match_start + match_length] == data[input_pos + match_length]):
                match_length += 1
            
            # Update best match
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = offset
        
        # Choose between literal or match encoding
        if best_match_length > 2:
            # Match: [high_offset, low_offset, length]
            compressed.extend([
                (best_match_offset >> 8) & 0xFF,  # High byte of offset
                best_match_offset & 0xFF,         # Low byte of offset
                best_match_length
            ])
            
            # Add to window
            window.extend(data[input_pos:input_pos + best_match_length])
            input_pos += best_match_length
        else:
            # Literal byte
            compressed.append(data[input_pos])
            window.append(data[input_pos])
            input_pos += 1
        
        # Maintain sliding window
        if len(window) > MAX_WINDOW:
            window = window[-MAX_WINDOW:]
    
    return bytes(compressed)

def lzrw_decompress(compressed_data):
    """
    Decompress data compressed with LZRW algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    if not compressed_data:
        return b''
    
    decompressed = bytearray()
    input_pos = 0
    
    while input_pos < len(compressed_data):
        # Insufficient data for full token
        if input_pos + 3 > len(compressed_data):
            # Treat as literal
            decompressed.append(compressed_data[input_pos])
            break
        
        # Decode token
        high_offset = compressed_data[input_pos]
        low_offset = compressed_data[input_pos + 1]
        length = compressed_data[input_pos + 2]
        
        if length == 0:
            # Literal byte
            decompressed.append(high_offset)
            input_pos += 1
        else:
            # Reference token
            offset = (high_offset << 8) | low_offset
            
            # Reconstruct sequence safely
            if len(decompressed) < offset:
                # Not enough previously decompressed data
                decompressed.append(compressed_data[input_pos])
                input_pos += 1
                continue
            
            ref_start = len(decompressed) - offset
            reconstructed = bytearray()
            
            # Safely copy previous sequence
            for j in range(length):
                if ref_start + j >= len(decompressed):
                    break
                byte = decompressed[ref_start + j]
                reconstructed.append(byte)
            
            # Append to decompressed data
            decompressed.extend(reconstructed)
            input_pos += 3
    
    return bytes(decompressed)