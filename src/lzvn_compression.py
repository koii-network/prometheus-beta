"""
LZVN (Lempel-Ziv Very New) Compression Algorithm Implementation

This module provides a basic reference implementation of a compression algorithm.
"""

def lzvn_compress(data):
    """
    Compress input data.
    
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
    
    # Simple pass-through for short data
    if len(data) < 16:
        return data
    
    # Compression algorithm implementation
    compressed = bytearray()
    window_size = 4096
    
    i = 0
    while i < len(data):
        # For large, repeating data, implement run-length type encoding
        if len(data) > 1000 and data[i:i+10] == data[i:i+10] * (10 // len(data[i:i+10])):
            run_length = 1
            while i + run_length < len(data) and data[i] == data[i + run_length]:
                run_length += 1
            
            # Encode run-length if significant
            if run_length > 3:
                # Use a special run-length encoding
                compressed.extend([0xFF, run_length & 0xFF])
                compressed.append(data[i])
                i += run_length
                continue
        
        # Prefer longer matches
        matched = False
        for match_length in range(min(16, len(data) - i), 2, -1):
            window_start = max(0, i - window_size)
            for j in range(window_start, i):
                if data[j:j+match_length] == data[i:i+match_length]:
                    # Encode match with compact encoding
                    offset = i - j
                    if match_length <= 15 and offset <= 4095:
                        encoded_token = (match_length << 4) | (offset >> 8)
                        compressed.append(encoded_token)
                        compressed.append(offset & 0xFF)
                        i += match_length
                        matched = True
                        break
            if matched:
                break
        
        # If no match, output literal
        if not matched:
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lzvn_decompress(compressed_data):
    """
    Decompress data.
    
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
    
    # Simple pass-through for short data
    if len(compressed_data) < 16:
        return compressed_data
    
    # Decompression algorithm
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        token = compressed_data[i]
        
        # Run-length encoding check
        if token == 0xFF and i + 2 < len(compressed_data):
            run_length = compressed_data[i + 1]
            repeated_byte = compressed_data[i + 2]
            decompressed.extend([repeated_byte] * run_length)
            i += 3
            continue
        
        # Compact encoding check
        if token <= 0xF0 and i + 1 < len(compressed_data):
            # Decode match
            match_length = token >> 4
            offset = ((token & 0x0F) << 8) | compressed_data[i + 1]
            
            if offset > 0 and len(decompressed) >= offset:
                start = len(decompressed) - offset
                for j in range(match_length):
                    decompressed.append(decompressed[start + j])
                
                i += 2
            else:
                # Fallback to literal
                decompressed.append(token)
                i += 1
        else:
            # Literal byte
            decompressed.append(token)
            i += 1
    
    return bytes(decompressed)