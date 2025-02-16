def lzw_compress(input_data):
    """
    Implement Lempel-Ziv-Welch (LZW) compression algorithm.
    
    Args:
        input_data (str or bytes): The input data to compress.
    
    Returns:
        list: A list of integer codes representing the compressed data.
    
    Raises:
        TypeError: If input is not a string or bytes.
    """
    # Validate input
    if not isinstance(input_data, (str, bytes)):
        raise TypeError("Input must be a string or bytes")
    
    # Convert input to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Initialize dictionary with single-character entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    result = []
    current_sequence = bytes()
    
    for byte in input_data:
        # Extend current sequence
        current_sequence += bytes([byte])
        
        # If the sequence is not in the dictionary, add a new entry
        if current_sequence not in dictionary:
            # Output the code for the sequence without the last character
            result.append(dictionary[current_sequence[:-1]])
            
            # Add new sequence to dictionary
            dictionary[current_sequence] = next_code
            next_code += 1
            
            # Reset current sequence to last character
            current_sequence = bytes([byte])
    
    # Output the last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzw_decompress(compressed_data):
    """
    Decompress data compressed with the LZW algorithm.
    
    Args:
        compressed_data (list): List of integer codes to decompress.
    
    Returns:
        bytes: The decompressed data.
    
    Raises:
        TypeError: If input is not a list of integers.
        ValueError: If compressed data is invalid.
    """
    # Validate input
    if not isinstance(compressed_data, list) or not all(isinstance(x, int) for x in compressed_data):
        raise TypeError("Input must be a list of integers")
    
    if not compressed_data:
        return bytes()
    
    # Validate first code
    if compressed_data[0] < 0 or compressed_data[0] > 255:
        raise ValueError("Invalid first code")
    
    # Initialize dictionary with single-character entries
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Decompression variables
    result = [dictionary[compressed_data[0]]]
    current_code = compressed_data[0]
    
    for code in compressed_data[1:]:
        # Validate code range
        if code < 0 or code >= next_code:
            raise ValueError(f"Invalid compressed code: {code}")
        
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            # Special case: current sequence + first character of current sequence
            current_entry = dictionary[current_code]
            entry = current_entry + current_entry[:1]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        result.append(entry)
        
        # Add new sequence to dictionary
        dictionary[next_code] = dictionary[current_code] + entry[:1]
        next_code += 1
        
        current_code = code
    
    return b''.join(result)