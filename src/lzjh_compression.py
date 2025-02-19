def lzjh_compress(data):
    """
    Implement the LZJH (Lempel-Ziv-Johnson-Hoan) compression algorithm.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    """
    # Initialize dictionary with single-byte entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    
    # Compression result
    compressed = []
    
    # Current sequence being processed
    current_sequence = b''
    
    for byte in data:
        # Try to extend the current sequence
        test_sequence = current_sequence + bytes([byte])
        
        if test_sequence in dictionary:
            # If sequence exists in dictionary, continue extending
            current_sequence = test_sequence
        else:
            # Output the code for the current sequence
            compressed.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not full
            if next_code < 65536:  # Limit dictionary size to 16-bit codes
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to the current byte
            current_sequence = bytes([byte])
    
    # Output the last sequence
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    # Convert to bytes
    return bytes(compressed)

def lzjh_decompress(compressed_data):
    """
    Decompress data compressed with the LZJH algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed original data
    """
    # Initialize dictionary with single-byte entries
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Decompression result
    decompressed = []
    
    # First code is always added
    current_code = compressed_data[0]
    result = dictionary[current_code]
    decompressed.extend(result)
    
    for code in compressed_data[1:]:
        # Determine the entry for the current code
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            # Special case: new sequence not yet in dictionary
            entry = dictionary[current_code] + dictionary[current_code][:1]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        # Add new entry to decompressed data
        decompressed.extend(entry)
        
        # Add new dictionary entry if not full
        if next_code < 65536:
            # New dictionary entry is previous entry + first byte of current entry
            dictionary[next_code] = dictionary[current_code] + entry[:1]
            next_code += 1
        
        # Update current code
        current_code = code
    
    return bytes(decompressed)