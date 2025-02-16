def lzc_compress(input_string):
    """
    Implement Lempel-Ziv-Cleary (LZC) compression algorithm.
    
    Args:
        input_string (str): The string to be compressed.
    
    Returns:
        list: A list of compressed codes representing the input string.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize dictionary with single-character entries
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    result = []
    current_sequence = ""
    
    for char in input_string:
        # Check if current sequence + next char exists in dictionary
        test_sequence = current_sequence + char
        
        if test_sequence in dictionary:
            # If sequence exists, extend current sequence
            current_sequence = test_sequence
        else:
            # Output code for current sequence
            result.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if room available
            if next_code < 65536:  # Limit dictionary size to prevent overflow
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to current character
            current_sequence = char
    
    # Output code for final sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result