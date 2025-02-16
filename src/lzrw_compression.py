def lzrw_compress(input_data):
    """
    Implement the LZRW (Lempel-Ziv Ross Williams) compression algorithm.
    
    Args:
        input_data (bytes): The input data to compress
    
    Returns:
        bytes: Compressed data
    """
    # Initialize compression parameters
    dictionary_size = 4096  # Typical sliding window size
    dictionary = {}
    compressed = bytearray()
    current_sequence = bytearray()
    
    # Iterate through input data
    for byte in input_data:
        # Try extending current sequence
        next_sequence = current_sequence + bytearray([byte])
        
        if bytes(next_sequence) in dictionary:
            # If sequence exists in dictionary, continue extending
            current_sequence = next_sequence
        else:
            # Output compression information
            if current_sequence:
                if len(current_sequence) == 1:
                    # Single byte literal
                    compressed.append(current_sequence[0])
                else:
                    # Find existing sequence in dictionary
                    match = dictionary.get(bytes(current_sequence), None)
                    if match is not None:
                        # Compressed reference (offset, length)
                        offset = match
                        compressed.extend([
                            (offset >> 8) & 0xFF,  # High byte of offset
                            offset & 0xFF,         # Low byte of offset
                            len(current_sequence)
                        ])
            
            # Add new sequence to dictionary
            if len(dictionary) < dictionary_size:
                dictionary[bytes(current_sequence)] = len(dictionary)
            
            # Reset current sequence to new byte
            current_sequence = bytearray([byte])
    
    # Handle final sequence
    if current_sequence:
        if len(current_sequence) == 1:
            compressed.append(current_sequence[0])
        else:
            match = dictionary.get(bytes(current_sequence), None)
            if match is not None:
                offset = match
                compressed.extend([
                    (offset >> 8) & 0xFF,
                    offset & 0xFF,
                    len(current_sequence)
                ])
    
    return bytes(compressed)

def lzrw_decompress(compressed_data):
    """
    Decompress data compressed with the LZRW algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Check if it's a literal byte
        if i + 3 > len(compressed_data):
            # If not enough data for a full token, treat as literals
            decompressed.append(compressed_data[i])
            i += 1
            continue
        
        # Check if it's a reference or a literal
        high_offset = compressed_data[i]
        low_offset = compressed_data[i+1]
        length = compressed_data[i+2]
        
        if length == 0:
            # Literal byte
            decompressed.append(high_offset)
            i += 1
        else:
            # Reference compression token
            offset = (high_offset << 8) | low_offset
            
            # Copy previous sequence
            start = len(decompressed) - offset
            for j in range(length):
                if start + j < 0:
                    break
                decompressed.append(decompressed[start + j])
            
            i += 3
    
    return bytes(decompressed)