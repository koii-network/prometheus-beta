def lzc_compress(data):
    """
    Implement Lempel-Ziv-Cattaneo (LZC) compression algorithm.
    
    Args:
        data (bytes or str): Input data to compress
    
    Returns:
        list: Compressed data as a list of integers representing dictionary entries
    """
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Initialize dictionary with single-byte entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    result = []
    current_sequence = b''
    
    for byte in data:
        # Construct potential new sequence
        potential_sequence = current_sequence + bytes([byte])
        
        # If sequence is in dictionary, extend current sequence
        if potential_sequence in dictionary:
            current_sequence = potential_sequence
        else:
            # Output code for current sequence
            result.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not full
            if next_code < 65536:  # Limit dictionary size
                dictionary[potential_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to current byte
            current_sequence = bytes([byte])
    
    # Output final sequence if not empty
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzc_decompress(compressed_data):
    """
    Decompress data compressed with Lempel-Ziv-Cattaneo algorithm.
    
    Args:
        compressed_data (list): Compressed data as list of integer codes
    
    Returns:
        bytes: Decompressed data
    """
    # Initialize dictionary with single-byte entries
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Decompression variables
    result = []
    previous_code = compressed_data[0]
    result.extend(dictionary[previous_code])
    
    for code in compressed_data[1:]:
        # Check if code is already in dictionary
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            # Special case: new sequence based on previous
            entry = dictionary[previous_code] + bytes([dictionary[previous_code][0]])
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        # Output current entry
        result.extend(entry)
        
        # Add new dictionary entry if not full
        if next_code < 65536:
            # New entry is previous sequence + first byte of current entry
            new_entry = dictionary[previous_code] + bytes([entry[0]])
            dictionary[next_code] = new_entry
            next_code += 1
        
        previous_code = code
    
    return bytes(result)