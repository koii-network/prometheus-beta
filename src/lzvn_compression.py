"""
LZVN (Lempel-Ziv Very New) Compression Algorithm Implementation

This module provides a basic implementation of the LZVN compression algorithm.
LZVN is a variant of LZ compression used in some compression scenarios.
"""

def lzvn_compress(data):
    """
    Compress input data using a basic LZVN-like compression algorithm.
    
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
    i = 0
    while i < len(data):
        # Look-ahead buffer to find repeated sequences
        look_ahead = min(16, len(data) - i)  # Max look-ahead of 16 bytes
        
        # Find longest match
        best_length = 1
        best_offset = 0
        for length in range(look_ahead, 0, -1):
            for j in range(max(0, i - 4096), i):  # Search back up to 4096 bytes
                if data[j:j+length] == data[i:i+length]:
                    offset = i - j
                    if offset > 0 and length > best_length:
                        best_length = length
                        best_offset = offset
                    break
        
        # Encode the result
        if best_length > 2:
            # Compressed token (offset, length)
            # Use variable-length encoding to save space
            if best_length <= 15 and best_offset <= 4095:
                compressed.append((best_length << 4) | (best_offset >> 8))
                compressed.append(best_offset & 0xFF)
            else:
                # Extended encoding for longer matches
                compressed.append(0xF0)
                compressed.append(best_length)
                compressed.append(best_offset >> 8)
                compressed.append(best_offset & 0xFF)
            
            i += best_length
        else:
            # Literal byte
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lzvn_decompress(compressed_data):
    """
    Decompress data compressed with the LZVN-like algorithm.
    
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
        # Check if it's a compressed token or literal
        token = compressed_data[i]
        
        if token == 0xF0 and i + 3 < len(compressed_data):
            # Extended encoding
            length = compressed_data[i + 1]
            offset = (compressed_data[i + 2] << 8) | compressed_data[i + 3]
            i += 4
        elif token <= 0xF0:
            # Standard encoding
            length = token >> 4
            offset = ((token & 0x0F) << 8) | compressed_data[i + 1]
            i += 2
        else:
            # Literal byte
            decompressed.append(token)
            i += 1
            continue
        
        # Copy matched sequence
        if length > 0 and offset > 0:
            start = len(decompressed) - offset
            for j in range(length):
                decompressed.append(decompressed[start + j])
    
    return bytes(decompressed)