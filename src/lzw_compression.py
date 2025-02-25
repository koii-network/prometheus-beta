"""
Lempel-Ziv-Welch (LZW) Compression Algorithm Implementation

This module provides functions for LZW compression and decompression.
"""

def lzw_compress(input_data):
    """
    Compress input data using the Lempel-Ziv-Welch (LZW) algorithm.
    
    Args:
        input_data (str): The input string to be compressed.
    
    Returns:
        list: A list of compressed integer codes.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Validate input
    if not isinstance(input_data, str):
        raise TypeError("Input must be a string")
    
    if not input_data:
        raise ValueError("Input cannot be an empty string")
    
    # Initialize dictionary with single-character strings
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    current_string = input_data[0]
    compressed = []
    
    # Compress the input
    for char in input_data[1:]:
        # Try to find current string + next char in dictionary
        test_string = current_string + char
        
        if test_string in dictionary:
            # If found, extend current string
            current_string = test_string
        else:
            # Output code for current string
            compressed.append(dictionary[current_string])
            
            # Add new string to dictionary
            dictionary[test_string] = next_code
            next_code += 1
            
            # Reset current string to current character
            current_string = char
    
    # Output code for last string
    if current_string:
        compressed.append(dictionary[current_string])
    
    return compressed

def lzw_decompress(compressed_data):
    """
    Decompress data previously compressed with LZW algorithm.
    
    Args:
        compressed_data (list): A list of integer codes to decompress.
    
    Returns:
        str: The decompressed original string.
    
    Raises:
        TypeError: If input is not a list of integers.
        ValueError: If input list is empty.
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of integers")
    
    if not compressed_data:
        raise ValueError("Input cannot be an empty list")
    
    # Initialize dictionary with single-character strings
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    # First code is always output as-is
    result = [dictionary[compressed_data[0]]]
    current_code = compressed_data[0]
    
    # Decompress the remaining codes
    for code in compressed_data[1:]:
        # Retrieve string for current code from dictionary
        if code in dictionary:
            current_string = dictionary[code]
        elif code == next_code:
            # Special case: code not yet in dictionary
            current_string = dictionary[current_code] + dictionary[current_code][0]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        # Output current string
        result.append(current_string)
        
        # Add new entry to dictionary
        if current_code in dictionary:
            dictionary[next_code] = dictionary[current_code] + current_string[0]
            next_code += 1
        
        current_code = code
    
    return ''.join(result)