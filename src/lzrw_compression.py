def lzrw_compress(input_data):
    """
    Implement LZRW (Lempel-Ziv Recompressing Wyllys) compression algorithm.
    
    Args:
        input_data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    """
    # Initialize compression variables
    dictionary = {}
    current_code = 256  # Start codes after ASCII characters
    compressed_data = []
    
    # Handle empty input
    if not input_data:
        return bytes()
    
    # Convert input to a list of bytes if it's not already
    if not isinstance(input_data, (bytes, bytearray)):
        input_data = input_data.encode()
    
    # Compression logic
    current_sequence = input_data[0:1]
    for byte in input_data[1:]:
        # Create a new sequence by appending the current byte
        candidate_sequence = current_sequence + bytes([byte])
        
        # If sequence exists in dictionary, extend current sequence
        if candidate_sequence in dictionary or len(candidate_sequence) == 1:
            current_sequence = candidate_sequence
        else:
            # Output the code for the current sequence
            if len(current_sequence) == 1:
                compressed_data.append(current_sequence[0])
            else:
                compressed_data.append(dictionary.get(current_sequence, -1))
            
            # Add new sequence to dictionary
            if current_code < 65536:  # Limit dictionary size
                dictionary[candidate_sequence] = current_code
                current_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Handle last sequence
    if len(current_sequence) == 1:
        compressed_data.append(current_sequence[0])
    else:
        compressed_data.append(dictionary.get(current_sequence, -1))
    
    # Convert to bytes
    return bytes(compressed_data)

def lzrw_decompress(compressed_data):
    """
    Decompress data compressed with LZRW algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    # Handle empty input
    if not compressed_data:
        return bytes()
    
    # Convert input to list of bytes if needed
    if not isinstance(compressed_data, (bytes, bytearray)):
        compressed_data = bytes(compressed_data)
    
    # Initialize decompression variables
    dictionary = {i: bytes([i]) for i in range(256)}
    current_code = 256
    decompressed_data = []
    
    # First byte
    current_entry = bytes([compressed_data[0]])
    decompressed_data.extend(current_entry)
    
    # Decompress remaining data
    for code in compressed_data[1:]:
        # If code is in dictionary, use its value
        if code in dictionary:
            next_entry = dictionary[code]
        # If it's the new code we just added, special case
        elif code == current_code:
            next_entry = current_entry + current_entry[0:1]
        else:
            raise ValueError(f"Invalid compressed data at code {code}")
        
        # Add to decompressed data
        decompressed_data.extend(next_entry)
        
        # Add new dictionary entry if possible
        if current_code < 65536:
            dictionary[current_code] = current_entry + next_entry[0:1]
            current_code += 1
        
        # Update current entry
        current_entry = next_entry
    
    return bytes(decompressed_data)