def lzrw_compress(input_data):
    """
    Implement the LZRW (Lempel-Ziv Ross Williams) compression algorithm.
    
    Args:
        input_data (bytes): The input data to compress.
    
    Returns:
        bytes: Compressed data.
    """
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not input_data:
        return b''
    
    # Initialize compression variables
    compressed = bytearray()
    window_size = 4096  # Typical window size for LZRW
    window_mask = window_size - 1
    
    # Compression flags and control variables
    output_index = 0
    input_index = 0
    
    while input_index < len(input_data):
        # Control byte to indicate literal or compressed segments
        control_byte_index = len(compressed)
        compressed.append(0)  # Placeholder for control byte
        control_byte = 0
        
        # Process 8 segments of data
        for bit in range(8):
            if input_index >= len(input_data):
                break
            
            # Look back in the window for match
            best_length = 0
            best_offset = 0
            
            for offset in range(1, min(window_size, input_index + 1)):
                match_length = 0
                look_behind = input_index - offset
                
                # Check for matching bytes
                while (input_index + match_length < len(input_data) and 
                       match_length < 255 and 
                       input_data[look_behind + match_length] == input_data[input_index + match_length]):
                    match_length += 1
                
                # Update best match
                if match_length > best_length:
                    best_length = match_length
                    best_offset = offset
            
            if best_length > 2:  # Compression is worth it
                # Encode offset and length
                compressed.append(((best_offset - 1) >> 8) & 0xFF)
                compressed.append((best_offset - 1) & 0xFF)
                compressed.append(best_length - 1)
                input_index += best_length
                control_byte |= (1 << (7 - bit))  # Set bit for compressed segment
            else:
                # Literal byte
                compressed.append(input_data[input_index])
                input_index += 1
        
        # Update control byte
        compressed[control_byte_index] = control_byte
    
    return bytes(compressed)

def lzrw_decompress(compressed_data):
    """
    Decompress data compressed with the LZRW algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data.
    
    Returns:
        bytes: Decompressed data.
    """
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        return b''
    
    decompressed = bytearray()
    input_index = 0
    
    while input_index < len(compressed_data):
        # Read control byte
        control_byte = compressed_data[input_index]
        input_index += 1
        
        # Process 8 segments
        for bit in range(8):
            if input_index >= len(compressed_data):
                break
            
            if control_byte & (1 << (7 - bit)):  # Compressed segment
                if input_index + 2 >= len(compressed_data):
                    break
                
                # Extract offset and length
                offset = ((compressed_data[input_index] << 8) | compressed_data[input_index + 1]) + 1
                length = compressed_data[input_index + 2] + 1
                input_index += 3
                
                # Copy matched segment
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
            else:  # Literal byte
                decompressed.append(compressed_data[input_index])
                input_index += 1
    
    return bytes(decompressed)