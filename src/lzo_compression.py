"""
Lempel-Ziv-Oberhumer (LZO) Compression Implementation

This module provides a basic implementation of LZO compression algorithm.
LZO is designed for speed and low memory consumption.
"""

def lzo_compress(data):
    """
    Compress input data using a simplified LZO-like compression algorithm.
    
    Args:
        data (bytes or bytearray): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input data is empty
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compression logic - simplified LZO-like approach
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Look for repeating sequences
        best_length = 1
        best_offset = 0
        
        # Search back 4096 bytes (typical LZO window size)
        search_start = max(0, i - 4096)
        for j in range(search_start, i):
            # Check potential match
            match_length = 0
            while (i + match_length < len(data) and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # Encode match or literal
        if best_length > 2:
            # Encode match (offset, length)
            compressed.extend([
                (best_offset >> 8) & 0xFF,  # High byte of offset
                best_offset & 0xFF,         # Low byte of offset
                best_length
            ])
            i += best_length
        else:
            # Encode literal
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lzo_decompress(compressed_data):
    """
    Decompress data compressed with the LZO-like algorithm.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input data is empty or corrupted
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # Decompression logic
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Check for match sequence
        if i + 2 < len(compressed_data):
            # Try to read offset and length
            offset = (compressed_data[i] << 8) | compressed_data[i+1]
            length = compressed_data[i+2]
            
            # Valid match sequence
            if offset > 0 and length > 0 and offset <= len(decompressed):
                # Prepare to copy matched sequence
                match_start = len(decompressed) - offset
                
                # Copy the matched sequence
                for j in range(length):
                    if match_start + j < 0 or match_start + j >= len(decompressed):
                        raise ValueError("Corrupt compressed data")
                    decompressed.append(decompressed[match_start + j])
                
                # Move past match sequence
                i += 3
                continue
        
        # Literal byte
        if i < len(compressed_data):
            decompressed.append(compressed_data[i])
        
        i += 1
    
    return bytes(decompressed)