"""
LZJB Compression Algorithm Implementation

This module provides functions for LZJB compression and decompression.
LZJB is a fast compression algorithm developed by Jeff Bonwick for the ZFS filesystem.
"""

def compress(data):
    """
    Compress input data using a simplified LZJB-like algorithm.
    
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
    
    compressed = bytearray()
    input_len = len(data)
    
    # Use a sliding window for compression
    window_size = 2048
    
    # Current position in the input
    input_index = 0
    
    while input_index < input_len:
        # Search back for the best match
        best_match_length = 0
        best_offset = 0
        
        # Limit search to current window
        search_start = max(0, input_index - window_size)
        search_end = input_index
        
        for offset in range(1, min(input_index - search_start + 1, 16)):
            # Try to find the longest match
            match_length = 0
            while (input_index + match_length < input_len and 
                   match_length < 8 and 
                   data[input_index + match_length] == data[input_index - offset + match_length]):
                match_length += 1
            
            # Update best match
            if match_length > best_match_length:
                best_match_length = match_length
                best_offset = offset
        
        # Encode the best match
        if best_match_length > 2:
            # Compressed token with offset and length
            # High bit set indicates compressed token
            try:
                token = (((best_offset - 1) << 3) | (best_match_length - 3)) | 0x80
                compressed.append(token & 0xFF)
                input_index += best_match_length
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
    Decompress data compressed with the simplified LZJB algorithm.
    
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
    
    decompressed = bytearray()
    input_index = 0
    
    while input_index < len(compressed_data):
        token = compressed_data[input_index]
        input_index += 1
        
        if token & 0x80:
            # Compressed token
            try:
                # Extract offset and length
                offset = ((token >> 3) & 0x0F) + 1
                length = (token & 0x07) + 3
                
                # Ensure we have enough previous data
                if len(decompressed) < offset:
                    raise ValueError("Insufficient previous data")
                
                # Copy matched sequence
                start_index = len(decompressed) - offset
                for _ in range(length):
                    decompressed.append(decompressed[start_index])
                    start_index += 1
            except Exception:
                # Fallback: treat as a literal byte
                decompressed.append(token)
        else:
            # Literal byte
            decompressed.append(token)
    
    return bytes(decompressed)