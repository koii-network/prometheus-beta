def lzjh_compress(input_data):
    """
    Implement an enhanced LZJH (Lempel-Ziv-Johnson-Huang) compression algorithm.
    
    Args:
        input_data (str or bytes): The input data to compress.
    
    Returns:
        list: Compressed representation of the input data.
    """
    # Convert input to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Initialize compression dictionary and output
    dictionary = {bytes([i]): i for i in range(256)}
    current_code = 256
    result = []
    current_sequence = b''
    
    # Iterate through the input bytes
    for byte in input_data:
        test_sequence = current_sequence + bytes([byte])
        
        if test_sequence in dictionary:
            # If sequence exists, keep extending
            current_sequence = test_sequence
        else:
            # Output code for current sequence
            if current_sequence:
                result.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if possible
            if current_code < 65536:  # Limit dictionary size
                dictionary[test_sequence] = current_code
                current_code += 1
            
            # Reset current sequence to current byte
            current_sequence = bytes([byte])
    
    # Handle last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzjh_decompress(compressed_data):
    """
    Decompress data compressed by LZJH algorithm.
    
    Args:
        compressed_data (list): Compressed representation.
    
    Returns:
        bytes: Decompressed data.
    """
    # Initialize decompression dictionary
    dictionary = {i: bytes([i]) for i in range(256)}
    current_code = 256
    result = bytearray()
    
    # Handling empty input
    if not compressed_data:
        return b''
    
    # First code is always a single byte
    current_sequence = dictionary[compressed_data[0]]
    result.extend(current_sequence)
    
    # Process remaining codes
    for code in compressed_data[1:]:
        if code in dictionary:
            # Code exists in dictionary
            next_sequence = dictionary[code]
        elif code == current_code:
            # Special case: repeated sequence
            next_sequence = current_sequence + current_sequence[0:1]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        result.extend(next_sequence)
        
        # Add new sequence to dictionary
        if current_code < 65536:
            dictionary[current_code] = current_sequence + next_sequence[0:1]
            current_code += 1
        
        current_sequence = next_sequence
    
    return bytes(result)