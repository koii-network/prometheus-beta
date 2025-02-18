def lzw_compress(input_data):
    """
    Implement Lempel-Ziv-Welch (LZW) compression algorithm.
    
    Args:
        input_data (str): The input string to be compressed.
    
    Returns:
        list: A list of integer codes representing the compressed data.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Input validation
    if not isinstance(input_data, str):
        raise TypeError("Input must be a string")
    
    if not input_data:
        raise ValueError("Input string cannot be empty")
    
    # Initialize dictionary with single-character strings
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    # Compression process
    result = []
    current_sequence = input_data[0]
    
    for char in input_data[1:]:
        # Check if current sequence + next char is in dictionary
        test_sequence = current_sequence + char
        
        if test_sequence in dictionary:
            # If sequence exists, continue building it
            current_sequence = test_sequence
        else:
            # Output the code for current sequence
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