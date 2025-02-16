import struct

def lz4_compress(input_data):
    """
    Implement a simplified LZ4 compression algorithm.
    
    Args:
        input_data (bytes): The input data to compress
    
    Returns:
        bytes: Compressed data
    """
    # Initialize compression variables
    compressed = bytearray()
    window_size = 65535  # Maximum window size
    
    # Convert input to bytes if it's not already
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate input
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or string")
    
    # Empty input case
    if not input_data:
        return bytes()
    
    # Compression logic
    i = 0
    while i < len(input_data):
        # Look for matching sequences
        best_match_length = 0
        best_match_offset = 0
        
        # Search back in the window for longest match
        search_start = max(0, i - window_size)
        for j in range(search_start, i):
            match_length = 0
            
            # Check how long the match continues
            while (i + match_length < len(input_data) and 
                   input_data[j + match_length] == input_data[i + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # Update best match if found
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = i - j
        
        # Encode the result
        if best_match_length >= 4:
            # Compressed sequence
            token = (best_match_offset & 0xFFFF) | ((best_match_length - 4) << 16)
            compressed.extend(struct.pack('<I', token))
            i += best_match_length
        else:
            # Literal byte
            compressed.append(input_data[i])
            i += 1
    
    return bytes(compressed)

def lz4_decompress(compressed_data):
    """
    Implement a simplified LZ4 decompression algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to decompress
    
    Returns:
        bytes: Decompressed data
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Empty input case
    if not compressed_data:
        return bytes()
    
    # Initialize decompression variables
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Read token
        token = struct.unpack('<I', compressed_data[i:i+4])[0]
        i += 4
        
        # Extract match offset and length
        match_offset = token & 0xFFFF
        match_length = ((token >> 16) & 0xFF) + 4
        
        # Copy matched sequence
        if match_length > 0:
            start = len(decompressed) - match_offset
            for j in range(match_length):
                decompressed.append(decompressed[start + j])
        else:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return bytes(decompressed)