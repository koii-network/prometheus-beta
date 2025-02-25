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
    window_size = 8192  # Expanded window size
    look_ahead_buffer = 32  # Expanded look-ahead buffer
    
    # Compression logic
    i = 0
    while i < len(data):
        # Non-repeated part
        if i + look_ahead_buffer >= len(data):
            # Append remaining bytes as literals
            compressed.append(data[i])
            i += 1
            continue
        
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
            try:
                compressed.extend([
                    best_offset & 0xFF,  # Lower byte of offset
                    ((best_offset >> 8) & 0x0F) | ((best_length - 3) << 4)  # Offset high + length
                ])
                i += best_length
            except ValueError:
                # Fallback to literal if encoding fails
                compressed.append(data[i])
                i += 1
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
        # Extend non-match (literal) encoding
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
            
            # Validate and copy matched sequence safely
            start = len(decompressed) - offset
            
            # Ensure start is valid
            if start < 0:
                decompressed.append(compressed_data[i])
                i += 1
                continue
            
            # Copy matched sequence
            for j in range(length):
                if start + j >= len(decompressed):
                    break
                decompressed.append(decompressed[start + j])
            
            i += 2
        except Exception:
            # Fallback to literal if decoding fails
            decompressed.append(compressed_data[i])
            i += 1
    
    return decompressed