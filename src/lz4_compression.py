"""
LZ4 Compression Algorithm Implementation

This module provides a simplified implementation of the LZ4 compression algorithm.
LZ4 is a lossless compression algorithm that focuses on compression and 
decompression speed while maintaining reasonable compression ratios.

Note: This is a basic implementation and does not cover all advanced LZ4 features.
"""

def lz4_compress(data):
    """
    Perform LZ4 compression on the input data.
    
    Args:
        data (bytes or str): The input data to compress.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compressed output will store the compressed data
    compressed = bytearray()
    
    # Current position in the input data
    pos = 0
    
    while pos < len(data):
        # Find the longest match in the previous data
        best_match_length = 0
        best_match_offset = 0
        
        # Look back up to 65535 bytes (16-bit offset)
        look_back = min(pos, 65535)
        
        for offset in range(1, look_back + 1):
            # Start of potential match
            match_start = pos - offset
            current_match_length = 0
            
            # Check how long the match continues
            while (pos + current_match_length < len(data) and 
                   data[match_start + current_match_length] == data[pos + current_match_length] and 
                   current_match_length < 255):
                current_match_length += 1
            
            # Update best match if found a longer match
            if current_match_length > best_match_length:
                best_match_length = current_match_length
                best_match_offset = offset
        
        # If no match found, store as literal
        if best_match_length < 4:
            compressed.append(data[pos])
            pos += 1
        else:
            # Encode match with offset and length
            compressed.extend([
                best_match_length - 4,  # Subtract 4 to save bits
                best_match_offset & 0xFF,   # Low byte of offset
                (best_match_offset >> 8) & 0xFF  # High byte of offset
            ])
            pos += best_match_length
    
    return bytes(compressed)

def lz4_decompress(compressed_data):
    """
    Decompress LZ4 compressed data.
    
    Args:
        compressed_data (bytes): The compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or invalid.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Decompressed output
    decompressed = bytearray()
    
    # Current position in compressed data
    pos = 0
    
    while pos < len(compressed_data):
        # Check if it's a literal or a match
        if compressed_data[pos] < 15:
            # Literal byte
            decompressed.append(compressed_data[pos])
            pos += 1
        else:
            # Match encoding
            match_length = compressed_data[pos] - 4
            
            # Check if we have enough bytes for offset
            if pos + 2 >= len(compressed_data):
                raise ValueError("Invalid compressed data")
            
            # Extract offset (little-endian 16-bit)
            offset = compressed_data[pos + 1] | (compressed_data[pos + 2] << 8)
            
            # Copy matched sequence
            if offset > len(decompressed):
                raise ValueError("Invalid offset in compressed data")
            
            # Repeat the matched sequence
            for _ in range(match_length):
                # Find the byte to copy from previous data
                copy_pos = len(decompressed) - offset
                decompressed.append(decompressed[copy_pos])
            
            # Move to next token
            pos += 3
    
    return bytes(decompressed)