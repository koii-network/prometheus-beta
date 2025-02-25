"""
Lempel-Ziv-Oberhumer (LZO) Compression Implementation

This module provides a basic implementation of LZO compression algorithm.
The implementation follows the core principles of LZO: sliding window 
compression with efficient encoding of repeated sequences.
"""

def compress_lzo(data):
    """
    Compress input data using a basic LZO-inspired compression algorithm.
    
    Args:
        data (bytes or bytearray): Input data to be compressed
    
    Returns:
        bytearray: Compressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input data is empty
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if len(data) == 0:
        raise ValueError("Input data cannot be empty")
    
    # Compression variables
    compressed = bytearray()
    window_size = 4096  # Typical sliding window size
    look_ahead_buffer = 16  # Look-ahead buffer size
    
    # Compression logic
    i = 0
    while i < len(data):
        # Find longest match in previous window
        best_length = 0
        best_offset = 0
        
        # Search back in the window for longest repeated sequence
        window_start = max(0, i - window_size)
        for j in range(window_start, i):
            # Check potential match length
            match_length = 0
            while (i + match_length < len(data) and 
                   match_length < look_ahead_buffer and 
                   data[j + match_length] == data[i + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # Encode match or literal
        if best_length > 2:
            # Encode matched sequence
            compressed.extend([
                best_offset & 0xFF,  # Lower byte of offset
                ((best_offset >> 8) & 0x0F) | ((best_length - 3) << 4)  # Offset high + length
            ])
            i += best_length
        else:
            # Encode literal byte
            compressed.append(data[i])
            i += 1
    
    return compressed

def decompress_lzo(compressed_data):
    """
    Decompress data compressed with the corresponding LZO compression method.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytearray: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input data is empty
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if len(compressed_data) == 0:
        raise ValueError("Input data cannot be empty")
    
    # Decompression variables
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Non-match (literal) encoding
        if compressed_data[i] >= 32:
            decompressed.append(compressed_data[i])
            i += 1
            continue
        
        # Ensure we have enough bytes for match decoding
        if i + 1 >= len(compressed_data):
            decompressed.append(compressed_data[i])
            break
        
        # Match encoding
        try:
            offset = compressed_data[i]
            offset |= (compressed_data[i + 1] & 0x0F) << 8
            length = (compressed_data[i + 1] >> 4) + 3
            
            # Copy matched sequence safely
            start = len(decompressed) - offset
            
            # Validate offset
            if start < 0:
                decompressed.append(compressed_data[i])
                i += 1
                continue
            
            for j in range(length):
                # Protect against potential out-of-range access
                if start + j < 0 or start + j >= len(decompressed):
                    decompressed.append(compressed_data[i])
                    break
                decompressed.append(decompressed[start + j])
            
            i += 2
        except Exception:
            # Fallback to literal if decoding fails
            decompressed.append(compressed_data[i])
            i += 1
    
    return decompressed