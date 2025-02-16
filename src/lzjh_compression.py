def lzjh_compress(data):
    """
    Implement the LZJH (Lempel-Ziv-Jelinek-Hankerson) compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
    """
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Initialize compression dictionary and output
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    result = []
    current_sequence = b''
    
    # Compress the data
    for byte in data:
        # Extend current sequence
        current_sequence += bytes([byte])
        
        # If sequence not in dictionary, add it
        if current_sequence not in dictionary:
            # Output code for previous sequence
            result.append(dictionary[current_sequence[:-1]])
            
            # Add new sequence to dictionary if not full
            if next_code < 65536:  # Limit dictionary size
                dictionary[current_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to last byte
            current_sequence = bytes([byte])
    
    # Output last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    # Convert result to bytes
    return bytes(result)

def lzjh_decompress(compressed_data):
    """
    Decompress data compressed with the LZJH algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to decompress.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Initialize decompression dictionary
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Prepare result and input processing
    result = []
    current = dictionary[compressed_data[0]]
    result.extend(current)
    
    # Decompress the data
    for code in compressed_data[1:]:
        # Get entry from dictionary, or create new one
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current + bytes([current[0]])
        else:
            raise ValueError("Invalid compressed data")
        
        # Add entry to result
        result.extend(entry)
        
        # Add new dictionary entry if not full
        if next_code < 65536:
            dictionary[next_code] = current + bytes([entry[0]])
            next_code += 1
        
        # Update current sequence
        current = entry
    
    return bytes(result)