def lzw_compress(input_string):
    """
    Implement Lempel-Ziv-Welch (LZW) compression algorithm.
    
    Args:
        input_string (str): The input string to compress.
    
    Returns:
        list: A list of integer codes representing the compressed data.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize dictionary with single-character strings
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    # Compression
    result = []
    current_sequence = input_string[0]
    
    for char in input_string[1:]:
        # Try to extend the current sequence
        test_sequence = current_sequence + char
        
        if test_sequence in dictionary:
            # If sequence exists, continue building it
            current_sequence = test_sequence
        else:
            # Output the code for the current sequence
            result.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary
            dictionary[test_sequence] = next_code
            next_code += 1
            
            # Reset current sequence to last character
            current_sequence = char
    
    # Output the last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzw_decompress(compressed_data):
    """
    Implement Lempel-Ziv-Welch (LZW) decompression algorithm.
    
    Args:
        compressed_data (list): A list of integer codes to decompress.
    
    Returns:
        str: The decompressed original string.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If input list is empty or contains invalid codes.
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of integer codes")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Initialize dictionary with single-character strings
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    # Decompression
    result = []
    current_code = compressed_data[0]
    current_string = dictionary[current_code]
    result.append(current_string)
    
    for code in compressed_data[1:]:
        # Handling unknown code (not in dictionary)
        if code not in dictionary:
            current_string = dictionary[current_code]
            current_string += current_string[0]
        else:
            current_string = dictionary[code]
        
        # Add current string to result
        result.append(current_string)
        
        # Add new sequence to dictionary
        if current_code in dictionary:
            new_sequence = dictionary[current_code] + current_string[0]
            dictionary[next_code] = new_sequence
            next_code += 1
        
        current_code = code
    
    return ''.join(result)