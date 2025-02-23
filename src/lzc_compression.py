"""
Lempel-Ziv-Compressions (LZC) Compression Algorithm Implementation.

This module provides functions for LZC compression and decompression.
"""

def lzc_compress(input_data):
    """
    Perform LZC compression on the input data.
    
    Args:
        input_data (str or bytes): The input data to compress.
    
    Returns:
        list: A list of compressed tokens.
    
    Raises:
        TypeError: If input is not a string or bytes.
        ValueError: If input is empty.
    """
    # Validate input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be a string or bytes")
    
    # Initialize dictionary with single-byte entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    current_sequence = bytes()
    compressed_output = []
    
    # Compress the input
    for byte in input_data:
        # Create a new sequence by extending current sequence
        potential_sequence = current_sequence + bytes([byte])
        
        # If sequence exists in dictionary, update current sequence
        if potential_sequence in dictionary:
            current_sequence = potential_sequence
        else:
            # Output the code for current sequence
            compressed_output.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not full
            if next_code < 65536:  # Limit dictionary size
                dictionary[potential_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to current byte
            current_sequence = bytes([byte])
    
    # Output the last sequence
    if current_sequence:
        compressed_output.append(dictionary[current_sequence])
    
    return compressed_output

def lzc_decompress(compressed_data):
    """
    Decompress data compressed with LZC algorithm.
    
    Args:
        compressed_data (list): List of compressed tokens.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not a list of integers.
        ValueError: If input is empty or contains invalid tokens.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not all(isinstance(x, int) for x in compressed_data):
        raise TypeError("Compressed data must be a list of integers")
    
    # Initialize dictionary with single-byte entries
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Decompression variables
    decompressed_output = []
    current_code = compressed_data[0]
    current_sequence = dictionary[current_code]
    decompressed_output.extend(current_sequence)
    
    # Decompress the rest of the data
    for code in compressed_data[1:]:
        if code not in dictionary:
            # Special case: new code not yet in dictionary
            new_sequence = current_sequence + bytes([current_sequence[0]])
        else:
            new_sequence = dictionary[code]
        
        # Add new sequence to output
        decompressed_output.extend(new_sequence)
        
        # Update dictionary if not full
        if next_code < 65536:
            dictionary[next_code] = current_sequence + bytes([new_sequence[0]])
            next_code += 1
        
        # Update current sequence
        current_sequence = new_sequence
        current_code = code
    
    return bytes(decompressed_output)