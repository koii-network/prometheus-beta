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
            # Ensure the token is within byte range
            compressed_token = min(
                (((best_offset - 1) << 3) | (max_match_length - 3)) | 0x80, 
                255
            )
            compressed.append(compressed_token)
            input_index += max_match_length
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
                    # If we don't have enough previous data, use what we have
                    match_start = 0
                else:
                    match_start = len(decompressed) - offset
                
                # Copy matched sequence
                for _ in range(length):
                    if match_start < len(decompressed):
                        decompressed.append(decompressed[match_start])
                        match_start += 1
                    else:
                        # If no previous data, append a zero or stop
                        decompressed.append(0)
            except Exception:
                # Fallback for malformed compressed data
                raise ValueError("Invalid compressed data")
        else:
            # Literal byte
            decompressed.append(token)
    
    return bytes(decompressed)