def lzp_compress(data):
    """
    Implement LZP (Lempel-Ziv Prediction) compression algorithm.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    """
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        return b''
    
    # Initialize compression parameters
    context_bits = 8  # Size of context for prediction
    context_size = 2 ** context_bits
    context_mask = context_size - 1
    
    # Dictionaries to track context and prediction
    context_table = [0] * context_size
    compressed = bytearray()
    
    # Context initialization
    context = 0
    
    # Compress the data
    for byte in data:
        # Calculate context hash
        predicted_byte = context_table[context]
        
        # If predicted byte matches current byte, output 0 (match)
        if predicted_byte == byte:
            compressed.append(0)
        else:
            # Output 1 followed by the actual byte
            compressed.append(1)
            compressed.append(byte)
        
        # Update context table
        context_table[context] = byte
        
        # Update context for next iteration
        context = ((context << 1) & context_mask) | ((byte >> 7) & 1)
    
    return bytes(compressed)

def lzp_decompress(compressed_data):
    """
    Implement LZP (Lempel-Ziv Prediction) decompression algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        return b''
    
    # Initialize decompression parameters
    context_bits = 8  # Size of context for prediction
    context_size = 2 ** context_bits
    context_mask = context_size - 1
    
    # Dictionaries to track context and prediction
    context_table = [0] * context_size
    decompressed = bytearray()
    
    # Context initialization
    context = 0
    
    # Index to track position in compressed data
    i = 0
    
    while i < len(compressed_data):
        # Check if it's a match or literal
        if compressed_data[i] == 0:
            # Predicted byte matches
            byte = context_table[context]
        else:
            # Literal byte follows
            i += 1
            if i >= len(compressed_data):
                break
            byte = compressed_data[i]
        
        # Add byte to decompressed data
        decompressed.append(byte)
        
        # Update context table
        context_table[context] = byte
        
        # Update context for next iteration
        context = ((context << 1) & context_mask) | ((byte >> 7) & 1)
        
        i += 1
    
    return bytes(decompressed)