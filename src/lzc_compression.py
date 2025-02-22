def lzc_compress(input_data):
    """
    Implement Lempel-Ziv-Cleary (LZC) compression algorithm.
    
    Args:
        input_data (str or bytes): The input data to compress.
    
    Returns:
        list: A list of integer codes representing the compressed data.
    
    Raises:
        TypeError: If input is not a string or bytes.
        ValueError: If input is empty.
    """
    # Validate input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Convert input to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be a string or bytes")
    
    # Initialize dictionary with single-byte entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    compressed = []
    
    # Current sequence being processed
    current_sequence = bytes()
    
    for byte in input_data:
        # Try to extend the current sequence
        test_sequence = current_sequence + bytes([byte])
        
        # If sequence is in dictionary, update current sequence
        if test_sequence in dictionary:
            current_sequence = test_sequence
        else:
            # Output the code for the current sequence
            compressed.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not at max code
            if next_code < 65536:  # Limit dictionary size to 16-bit codes
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to current byte
            current_sequence = bytes([byte])
    
    # Output the last sequence
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    return compressed