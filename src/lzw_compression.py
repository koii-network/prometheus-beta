"""
Lempel-Ziv-Welch (LZW) Compression Algorithm Implementation

This module provides functions for LZW compression and decompression.
"""

def lzw_compress(data):
    """
    Compress the input data using the Lempel-Ziv-Welch (LZW) algorithm.
    
    Args:
        data (str): The input string to be compressed.
    
    Returns:
        list: A list of integer codes representing the compressed data.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Input validation
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    
    if not data:
        raise ValueError("Input string cannot be empty")
    
    # Initialize dictionary with single-character strings
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    # Compression process
    compressed = []
    current_sequence = ""
    
    for char in data:
        # Extend current sequence
        potential_sequence = current_sequence + char
        
        # If the sequence is in the dictionary, continue building
        if potential_sequence in dictionary:
            current_sequence = potential_sequence
        else:
            # Output the code for the current sequence
            compressed.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary
            dictionary[potential_sequence] = next_code
            next_code += 1
            
            # Reset current sequence to current character
            current_sequence = char
    
    # Add the last sequence if not empty
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    return compressed

def lzw_decompress(compressed):
    """
    Decompress data previously compressed using the LZW algorithm.
    
    Args:
        compressed (list): A list of integer codes representing compressed data.
    
    Returns:
        str: The original decompressed string.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If input list is empty or contains invalid codes.
    """
    # Input validation
    if not isinstance(compressed, list):
        raise TypeError("Input must be a list of integer codes")
    
    if not compressed:
        raise ValueError("Compressed data cannot be empty")
    
    # Validate first code
    if compressed[0] < 0 or compressed[0] > 255:
        raise ValueError(f"Invalid first code: {compressed[0]}")
    
    # Initialize dictionary with single-character strings
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    # First code
    result = [dictionary[compressed[0]]]
    current_code = compressed[0]
    
    # Decompression process
    for code in compressed[1:]:
        # If code is a known code in the dictionary
        if code in dictionary:
            current_string = dictionary[code]
        # If code is the next possible code (special case in LZW algorithm)
        elif code == next_code:
            current_string = dictionary[current_code] + dictionary[current_code][0]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        # Add to result
        result.append(current_string)
        
        # Add new dictionary entry 
        # Use the first character of the current string to extend previous code's string
        if current_code in dictionary:
            dictionary[next_code] = dictionary[current_code] + current_string[0]
            next_code += 1
        
        # Update current code
        current_code = code
    
    # Return decompressed string
    return ''.join(result)