def lzc_compress(data):
    """
    Implement Lempel-Ziv-Cleary (LZC) compression algorithm.
    
    Args:
        data (str or bytes): Input data to compress
    
    Returns:
        list: Compressed representation of the input data
    """
    if not data:
        return []
    
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Initialize dictionary with single-byte entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    current_sequence = bytes()
    result = []
    
    for byte in data:
        # Extend current sequence
        current_sequence += bytes([byte])
        
        # If sequence is not in dictionary, add it
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
    
    return result

def lzc_decompress(compressed_data):
    """
    Decompress data previously compressed with LZC algorithm.
    
    Args:
        compressed_data (list): Compressed data representation
    
    Returns:
        bytes: Decompressed data
    """
    if not compressed_data:
        return b''
    
    # Initialize dictionary with single-byte entries
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # First entry
    result = dictionary[compressed_data[0]]
    previous_code = compressed_data[0]
    
    for code in compressed_data[1:]:
        # Retrieve or generate current sequence
        if code in dictionary:
            current_sequence = dictionary[code]
        elif code == next_code:
            # Special case: new sequence not yet added
            current_sequence = dictionary[previous_code] + bytes([dictionary[previous_code][0]])
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        result += current_sequence
        
        # Add new dictionary entry if not full
        if next_code < 65536:
            dictionary[next_code] = dictionary[previous_code] + bytes([current_sequence[0]])
            next_code += 1
        
        previous_code = code
    
    return result