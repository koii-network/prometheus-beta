"""
Lempel-Ziv-Cleary (LZC) Compression Algorithm Implementation.

This module provides functions for LZC compression and decompression.
"""

def lzc_compress(input_data):
    """
    Compress input data using the Lempel-Ziv-Cleary compression algorithm.
    
    Args:
        input_data (str or bytes): The data to be compressed.
    
    Returns:
        list: Compressed data represented as a list of integer codes.
    
    Raises:
        TypeError: If input is not a string or bytes.
        ValueError: If input is empty.
    """
    # Convert input to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate input
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be a string or bytes")
    
    if not input_data:
        raise ValueError("Input cannot be empty")
    
    # Initialize dictionary with single-byte entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    max_code = 65536  # 16-bit dictionary limit
    
    result = []
    current_sequence = bytes([input_data[0]])
    
    for byte in input_data[1:]:
        # Try to extend the current sequence
        extended_sequence = current_sequence + bytes([byte])
        
        if extended_sequence in dictionary:
            # If sequence exists, continue building it
            current_sequence = extended_sequence
        else:
            # Output code for current sequence
            result.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not at max
            if next_code < max_code:
                dictionary[extended_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Output last sequence
    result.append(dictionary[current_sequence])
    
    return result

def lzc_decompress(compressed_data):
    """
    Decompress data compressed using the Lempel-Ziv-Cleary algorithm.
    
    Args:
        compressed_data (list): List of integer codes to decompress.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not a list of integers.
        ValueError: If input is empty or contains invalid codes.
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of integer codes")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Initialize dictionary with single-byte entries
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    max_code = 65536  # 16-bit dictionary limit
    
    result = []
    previous_code = compressed_data[0]
    result.extend(dictionary[previous_code])
    
    for code in compressed_data[1:]:
        if code not in dictionary:
            # Handle out-of-range codes
            if code >= next_code:
                raise ValueError(f"Invalid compression code: {code}")
        
        # Retrieve current sequence
        if code in dictionary:
            current_sequence = dictionary[code]
        else:
            # Special case for new sequence not yet in dictionary
            previous_sequence = dictionary[previous_code]
            current_sequence = previous_sequence + bytes([previous_sequence[0]])
        
        # Add current sequence to result
        result.extend(current_sequence)
        
        # Add new dictionary entry if not at max
        if next_code < max_code:
            # New entry is previous sequence + first byte of current sequence
            new_entry = dictionary[previous_code] + bytes([current_sequence[0]])
            dictionary[next_code] = new_entry
            next_code += 1
        
        previous_code = code
    
    return bytes(result)