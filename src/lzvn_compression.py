"""
LZVN (Lempel-Ziv Very New) Compression Algorithm Implementation

This module provides a basic implementation of the LZVN compression algorithm.
"""

def lzvn_compress(data):
    """
    Compress input data using a more robust compression algorithm.
    
    Args:
        data (bytes): The input data to compress
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    # Compression algorithm implementation
    compressed = bytearray()
    window_size = 4096
    max_match_length = 255
    
    i = 0
    while i < len(data):
        # Find the longest match in the sliding window
        longest_match_length = 0
        longest_match_offset = 0
        
        # Look back in the window to find longest match
        window_start = max(0, i - window_size)
        for j in range(window_start, i):
            match_length = 0
            while (i + match_length < len(data) and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < max_match_length):
                match_length += 1
            
            if match_length > longest_match_length:
                longest_match_length = match_length
                longest_match_offset = i - j
        
        # Encode match or literal
        if longest_match_length > 2:
            # Encode match with length and offset
            if longest_match_length <= 15 and longest_match_offset <= 4095:
                # Compact encoding
                encoded_token = (longest_match_length << 4) | (longest_match_offset >> 8)
                compressed.append(encoded_token)
                compressed.append(longest_match_offset & 0xFF)
            else:
                # Extended encoding
                compressed.append(0xF0)  # Extended token marker
                compressed.append(longest_match_length)
                compressed.append(longest_match_offset >> 8)
                compressed.append(longest_match_offset & 0xFF)
            
            # Move past the matched sequence
            i += longest_match_length
        else:
            # Literal byte
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lzvn_decompress(compressed_data):
    """
    Decompress data compressed with the LZVN algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or compressed data is invalid
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Decompression algorithm
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        token = compressed_data[i]
        
        # Literal byte
        if token > 0xF0 or i + 1 >= len(compressed_data):
            decompressed.append(token)
            i += 1
            continue
        
        # Match encoding
        if token == 0xF0 and i + 3 < len(compressed_data):
            # Extended encoding
            length = compressed_data[i + 1]
            offset = (compressed_data[i + 2] << 8) | compressed_data[i + 3]
            i += 4
        else:
            # Standard encoding
            length = token >> 4
            if i + 1 >= len(compressed_data):
                decompressed.append(token)
                break
            
            offset = ((token & 0x0F) << 8) | compressed_data[i + 1]
            i += 2
        
        # Safety checks for offset and length
        if offset <= 0 or length <= 0 or offset > len(decompressed):
            decompressed.append(token)
            continue
        
        # Reconstruct the matched sequence
        start = len(decompressed) - offset
        for j in range(length):
            decompressed.append(decompressed[start + j])
    
    return bytes(decompressed)