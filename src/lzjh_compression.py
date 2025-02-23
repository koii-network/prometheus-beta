"""
LZJH (Lempel-Ziv-Johnson-Hui) Compression Algorithm Implementation

This module provides functions for LZJH compression and decompression.
"""

def lzjh_compress(data):
    """
    Compress input data using the LZJH compression algorithm.
    
    Args:
        data (bytes or str): Input data to compress
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Initialize compression dictionary and output
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    result = bytearray()
    current_sequence = bytes()
    
    # Compression logic
    for byte in data:
        # Extend current sequence
        potential_sequence = current_sequence + bytes([byte])
        
        # If sequence exists in dictionary, update current sequence
        if potential_sequence in dictionary:
            current_sequence = potential_sequence
        else:
            # Output code for current sequence
            result.extend(dictionary[current_sequence].to_bytes(2, 'big'))
            
            # Add new sequence to dictionary if not full
            if next_code < 65536:  # 16-bit codes
                dictionary[potential_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Handle last sequence
    if current_sequence:
        result.extend(dictionary[current_sequence].to_bytes(2, 'big'))
    
    return bytes(result)

def lzjh_decompress(compressed_data):
    """
    Decompress data compressed with the LZJH algorithm.
    
    Args:
        compressed_data (bytes): Data to decompress
    
    Returns:
        bytes: Decompressed original data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or malformed
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Ensure input length is even (2-byte codes)
    if len(compressed_data) % 2 != 0:
        raise ValueError("Compressed data must have even length")
    
    # Ensure input has at least 2 bytes
    if len(compressed_data) < 2:
        raise ValueError("Compressed data is truncated")
    
    # Initialize decompression dictionary and output
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    result = bytearray()
    
    # Read first code
    current_code = int.from_bytes(compressed_data[:2], 'big')
    result.extend(dictionary[current_code])
    previous_sequence = dictionary[current_code]
    
    # Process remaining codes
    for i in range(2, len(compressed_data), 2):
        # Ensure we have 2 full bytes
        if i + 1 >= len(compressed_data):
            raise ValueError("Compressed data is truncated")
        
        # Read next code
        current_code = int.from_bytes(compressed_data[i:i+2], 'big')
        
        # Handle known and unknown cases
        if current_code in dictionary:
            current_sequence = dictionary[current_code]
            result.extend(current_sequence)
            
            # Create new dictionary entry
            if next_code < 65536:
                new_sequence = previous_sequence + bytes([current_sequence[0]])
                dictionary[next_code] = new_sequence
                next_code += 1
        else:
            # Special case: new sequence
            current_sequence = previous_sequence + bytes([previous_sequence[0]])
            result.extend(current_sequence)
            
            # Create new dictionary entry
            if next_code < 65536:
                dictionary[next_code] = current_sequence
                next_code += 1
        
        previous_sequence = current_sequence
    
    return bytes(result)