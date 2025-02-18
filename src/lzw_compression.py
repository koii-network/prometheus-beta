def lzw_compress(input_data):
    """
    Implement Lempel-Ziv-Welch (LZW) compression algorithm.
    
    Args:
        input_data (str): The input string to be compressed.
    
    Returns:
        list: A list of compressed codes representing the input data.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input
    if not isinstance(input_data, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return an empty list
    if not input_data:
        return []
    
    # Initialize dictionary with single-character strings
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    # Compression process
    compressed = []
    current_sequence = input_data[0]
    
    for char in input_data[1:]:
        # Check if current sequence + next character is in dictionary
        test_sequence = current_sequence + char
        
        if test_sequence in dictionary:
            # If sequence exists, extend current sequence
            current_sequence = test_sequence
        else:
            # Output code for current sequence
            compressed.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary
            dictionary[test_sequence] = next_code
            next_code += 1
            
            # Reset current sequence to last character
            current_sequence = char
    
    # Add the last sequence
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    return compressed

def lzw_decompress(compressed_data):
    """
    Decompress data compressed with LZW algorithm.
    
    Args:
        compressed_data (list): A list of compressed codes.
    
    Returns:
        str: The decompressed original string.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If compressed data is invalid.
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of integer codes")
    
    # If input is empty, return empty string
    if not compressed_data:
        return ""
    
    # Initialize dictionary with single-character strings
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    # Decompression process
    result = [chr(compressed_data[0])]
    current_code = compressed_data[0]
    
    for code in compressed_data[1:]:
        # Retrieve current sequence from dictionary
        if code in dictionary:
            current_sequence = dictionary[code]
        elif code == next_code:
            # Special case: first unseen code
            current_sequence = dictionary[current_code] + dictionary[current_code][0]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        # Add current sequence to result
        result.append(current_sequence)
        
        # Add new dictionary entry
        if current_code in dictionary:
            dictionary[next_code] = dictionary[current_code] + current_sequence[0]
            next_code += 1
        
        current_code = code
    
    return ''.join(result)