def lzc_compress(input_data):
    """
    Implement Lempel-Ziv-Cleary (LZC) compression algorithm.
    
    Args:
        input_data (str or bytes): The input data to compress
    
    Returns:
        list: Compressed data as a list of integer codes
    """
    # Convert input to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Initialize dictionary with single-byte entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    result = []
    current_sequence = b''
    
    for byte in input_data:
        # Try to extend the current sequence
        test_sequence = current_sequence + bytes([byte])
        
        if test_sequence in dictionary:
            # If the extended sequence is in the dictionary, continue
            current_sequence = test_sequence
        else:
            # Output the code for the current sequence
            result.append(dictionary[current_sequence])
            
            # Add the new sequence to the dictionary if not full
            if next_code < 65536:  # Limit dictionary size
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to the current byte
            current_sequence = bytes([byte])
    
    # Output the last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzc_decompress(compressed_data):
    """
    Decompress data compressed with the Lempel-Ziv-Cleary algorithm.
    
    Args:
        compressed_data (list): List of integer codes to decompress
    
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
        if code in dictionary:
            # Known code
            current_sequence = dictionary[code]
        elif code == next_code:
            # Special case: code just beyond dictionary
            previous_sequence = dictionary[previous_code]
            current_sequence = previous_sequence + previous_sequence[:1]
        else:
            raise ValueError(f"Invalid compression code: {code}")
        
        # Add current sequence to result
        result.extend(current_sequence)
        
        # Update dictionary if not full
        if next_code < 65536:
            # New entry is previous sequence + first byte of current sequence
            new_entry = dictionary[previous_code] + current_sequence[:1]
            dictionary[next_code] = new_entry
            next_code += 1
        
        previous_code = code
    
    return bytes(result)