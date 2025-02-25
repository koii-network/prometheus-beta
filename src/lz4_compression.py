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
        # Look for the longest match in previous data
        best_match_length = 0
        best_match_offset = 0
        
        # Search back up to 65535 bytes
        search_back = min(pos, 65535)
        
        for offset in range(1, search_back + 1):
            # Start of potential match
            match_start = pos - offset
            current_match_length = 0
            
            # Check match length
            while (pos + current_match_length < len(data) and 
                   data[match_start + current_match_length] == data[pos + current_match_length] and 
                   current_match_length < 255):
                current_match_length += 1
            
            # Update best match
            if current_match_length > best_match_length:
                best_match_length = current_match_length
                best_match_offset = offset
        
        # Encode the data
        if best_match_length < 4:
            # Literal byte
            compressed.append(data[pos])
            pos += 1
        else:
            # Encode match
            # Token = (match length - 4) in high 4 bits, offset in low 12 bits
            match_token = (best_match_length - 4) << 4
            match_token |= (best_match_offset & 0xFFF)
            
            # Write token bytes
            compressed.append((match_token >> 8) & 0xFF)
            compressed.append(match_token & 0xFF)
            
            # Move forward
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
        # Literal or match determination
        if compressed_data[pos] < 240:  # Assume literal
            decompressed.append(compressed_data[pos])
            pos += 1
        else:
            # Extract token
            if pos + 1 >= len(compressed_data):
                raise ValueError("Invalid compressed data")
            
            token = (compressed_data[pos] << 8) | compressed_data[pos + 1]
            
            # Extract match length (high 4 bits)
            match_length = (token >> 12) + 4
            
            # Extract offset (low 12 bits)
            offset = token & 0xFFF
            
            # Verify offset is valid
            if offset > len(decompressed):
                raise ValueError("Invalid offset in compressed data")
            
            # Copy matched sequence
            for _ in range(match_length):
                # Find the byte to copy from previous data
                copy_pos = len(decompressed) - offset
                decompressed.append(decompressed[copy_pos])
            
            # Move to next token
            pos += 2
    
    return bytes(decompressed)