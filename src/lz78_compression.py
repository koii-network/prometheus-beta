"""
LZ78 Compression Algorithm Implementation

This module provides functions for LZ78 compression and decompression.
LZ78 is a dictionary-based lossless compression algorithm that builds 
a dictionary of previously seen sequences during compression.
"""

from typing import List, Tuple


def lz78_compress(input_string: str) -> List[Tuple[int, str]]:
    """
    Compress the input string using the LZ78 compression algorithm.
    
    Args:
        input_string (str): The string to be compressed
    
    Returns:
        List[Tuple[int, str]]: A list of tuples representing compressed tokens
        Each tuple contains (dictionary_index, character)
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input string is empty
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize compression dictionary and output
    dictionary = {
        '': 0  # Empty string is the first entry in dictionary
    }
    output = []
    current_sequence = ''
    next_index = 1
    
    # Compress the input string
    for char in input_string:
        # Try to find the longest match in the dictionary
        test_sequence = current_sequence + char
        
        # If the sequence is not in the dictionary
        if test_sequence not in dictionary:
            # Output the token (index of previous match, new character)
            prefix_index = dictionary.get(current_sequence, 0)
            output.append((prefix_index, char))
            
            # Add the new sequence to the dictionary
            dictionary[test_sequence] = next_index
            next_index += 1
            
            # Reset current sequence
            current_sequence = ''
        else:
            # If the sequence is in the dictionary, continue building it
            current_sequence = test_sequence
    
    # Handle any remaining sequence
    if current_sequence:
        prefix_index = dictionary.get(current_sequence[:-1], 0)
        output.append((prefix_index, current_sequence[-1]))
    
    return output


def lz78_decompress(compressed_data: List[Tuple[int, str]]) -> str:
    """
    Decompress the LZ78 compressed data back to the original string.
    
    Args:
        compressed_data (List[Tuple[int, str]]): Compressed tokens from LZ78 compression
    
    Returns:
        str: The decompressed original string
    
    Raises:
        TypeError: If input is not a list of tuples
        ValueError: If compressed data is invalid
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of tuples")
    
    # Initialize dictionary and output
    dictionary = {0: ''}
    output = []
    next_index = 1
    
    # Decompress the tokens
    for index, char in compressed_data:
        # Retrieve the sequence for the given index
        try:
            prefix_sequence = dictionary[index]
        except KeyError:
            raise ValueError(f"Invalid dictionary index: {index}")
        
        # Construct the new sequence
        current_sequence = prefix_sequence + char
        output.append(current_sequence)
        
        # Add the new sequence to the dictionary
        dictionary[next_index] = current_sequence
        next_index += 1
    
    # Return the decompressed string
    return ''.join(output)