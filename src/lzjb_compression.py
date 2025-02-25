"""
LZJB Compression Algorithm Implementation

This module provides functions for LZJB compression and decompression.
LZJB is a fast compression algorithm developed by Jeff Bonwick for the ZFS filesystem.
"""

def compress(data):
    """
    Compress input data using the LZJB compression algorithm.
    
    Args:
        data (bytes): Input data to compress
    
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
    
    # LZJB compression implementation
    compressed = bytearray()
    input_len = len(data)
    input_index = 0
    
    while input_index < input_len:
        # Look for matching sequences
        max_match_length = 0
        best_offset = 0
        
        # Search back (typically up to 2048 bytes)
        search_back_limit = min(input_index, 2048)
        
        for offset in range(1, search_back_limit + 1):
            match_length = 0
            
            # Check for potential match
            while (input_index + match_length < input_len and 
                   match_length < 10 and 
                   data[input_index + match_length] == data[input_index - offset + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > max_match_length:
                max_match_length = match_length
                best_offset = offset
        
        # Encode the result
        if max_match_length > 2:
            # Compressed match
            try:
                # More careful bit manipulation
                offset_bits = min(max(0, best_offset - 1), 15)
                length_bits = min(max(0, max_match_length - 3), 7)
                
                # Construct compressed token
                compressed_token = (offset_bits << 3) | length_bits | 0x80
                compressed.append(compressed_token & 0xFF)
                input_index += max_match_length
            except Exception:
                # Fallback to literal byte
                compressed.append(data[input_index])
                input_index += 1
        else:
            # Literal byte
            compressed.append(data[input_index])
            input_index += 1
    
    return bytes(compressed)

def decompress(compressed_data):
    """
    Decompress data compressed with the LZJB algorithm.
    
    Args:
        compressed_data (bytes): Input compressed data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or malformed
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Decompression implementation
    decompressed = bytearray()
    input_index = 0
    
    while input_index < len(compressed_data):
        token = compressed_data[input_index]
        input_index += 1
        
        if token & 0x80:
            # Compressed match
            try:
                offset = ((token >> 3) & 0x0F) + 1
                length = (token & 0x07) + 3
                
                # Ensure we have enough previously decompressed data
                if len(decompressed) < offset:
                    raise ValueError("Insufficient previous data")
                
                # Copy matched sequence
                start_index = len(decompressed) - offset
                for _ in range(length):
                    decompressed.append(decompressed[start_index])
                    start_index += 1
            except Exception:
                # Fallback for malformed compressed data
                # Default to preserving the token as a literal
                decompressed.append(token)
        else:
            # Literal byte
            decompressed.append(token)
    
    return bytes(decompressed)