"""
Lempel-Ziv-Cleary (LZC) Compression Algorithm Implementation.

This module provides functions for LZC compression and decompression.
"""

def lzc_compress(data):
    """
    Compress input data using the Lempel-Ziv-Cleary compression algorithm.
    
    Args:
        data (str or bytes): The input data to compress.
    
    Returns:
        list: A list of integer codes representing the compressed data.
    
    Raises:
        TypeError: If input is not a string or bytes.
        ValueError: If input is empty.
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes")
    
    # Initialize dictionary with single-byte entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    max_code = 65536  # Limit dictionary size
    
    # Compression variables
    compressed = []
    current_sequence = bytes()
    
    for byte in data:
        # Extend current sequence
        test_sequence = current_sequence + bytes([byte])
        
        # If sequence is in dictionary, continue building
        if test_sequence in dictionary:
            current_sequence = test_sequence
        else:
            # Output code for current sequence
            compressed.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not at max code
            if next_code < max_code:
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Output last sequence
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    return compressed

def lzc_decompress(compressed_data):
    """
    Decompress data previously compressed with LZC algorithm.
    
    Args:
        compressed_data (list): List of integer codes to decompress.
    
    Returns:
        bytes: The decompressed data.
    
    Raises:
        TypeError: If input is not a list of integers.
        ValueError: If input is empty or contains invalid codes.
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of integer codes")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Initialize dictionary with single-byte entries
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    max_code = 65536  # Limit dictionary size
    
    # Decompression variables
    decompressed = []
    previous_code = compressed_data[0]
    decompressed.extend(dictionary[previous_code])
    
    for code in compressed_data[1:]:
        # Handle potential invalid codes
        if code not in dictionary:
            # Special case: current code not yet in dictionary
            current_sequence = dictionary[previous_code]
            current_sequence += current_sequence[0:1]
        else:
            current_sequence = dictionary[code]
        
        decompressed.extend(current_sequence)
        
        # Add new sequence to dictionary
        if next_code < max_code:
            dictionary[next_code] = dictionary[previous_code] + current_sequence[0:1]
            next_code += 1
        
        previous_code = code
    
    return bytes(decompressed)