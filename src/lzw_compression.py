def lzw_compress(input_string):
    """
    Implement Lempel-Ziv-Welch (LZW) compression algorithm.
    
    Args:
        input_string (str): The input string to compress
    
    Returns:
        list: Compressed representation of the input string
    """
    # Handle empty input
    if not input_string:
        return []
    
    # Initialize dictionary with single-character strings
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    # Initialize compression variables
    result = []
    current_sequence = input_string[0]
    
    # Compress the input string
    for char in input_string[1:]:
        # Check if current sequence + next char is in dictionary
        test_sequence = current_sequence + char
        
        if test_sequence in dictionary:
            # If sequence exists, extend current sequence
            current_sequence = test_sequence
        else:
            # Output code for current sequence
            result.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary
            dictionary[test_sequence] = next_code
            next_code += 1
            
            # Reset current sequence to last character
            current_sequence = char
    
    # Output code for last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzw_decompress(compressed_data):
    """
    Implement Lempel-Ziv-Welch (LZW) decompression algorithm.
    
    Args:
        compressed_data (list): Compressed representation of the input string
    
    Returns:
        str: Decompressed original string
    """
    # Handle empty input
    if not compressed_data:
        return ""
    
    # Initialize dictionary with single-character strings
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    # Initialize decompression variables
    result = [dictionary[compressed_data[0]]]
    current_sequence = result[0]
    
    # Decompress the compressed data
    for code in compressed_data[1:]:
        # Determine the string for the current code
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            # Special case: new sequence not yet in dictionary
            entry = current_sequence + current_sequence[0]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        # Add entry to result
        result.append(entry)
        
        # Add new sequence to dictionary
        dictionary[next_code] = current_sequence + entry[0]
        next_code += 1
        
        # Update current sequence
        current_sequence = entry
    
    return ''.join(result)