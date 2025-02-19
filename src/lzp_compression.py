def lzp_compress(data):
    """
    Implement Lempel-Ziv Prediction (LZP) compression algorithm.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        return b''
    
    # Initialize prediction context and output
    context_size = 256  # Context size for prediction
    context = [0] * context_size
    context_index = 0
    compressed = bytearray()
    
    # Iterate through input data
    for byte in data:
        # Predict next byte based on previous context
        predicted = context[context_index]
        
        # If prediction is incorrect, output a flag and the actual byte
        if byte != predicted:
            compressed.append(0xFF)  # Mismatch flag
            compressed.append(byte)
        
        # Update context
        context[context_index] = byte
        context_index = (context_index + 1) % context_size
    
    return bytes(compressed)

def lzp_decompress(compressed_data):
    """
    Decompress data compressed with LZP algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        return b''
    
    # Initialize prediction context and output
    context_size = 256
    context = [0] * context_size
    context_index = 0
    decompressed = bytearray()
    
    i = 0
    while i < len(compressed_data):
        # Check for mismatch flag
        if compressed_data[i] == 0xFF:
            # Next byte is the actual value
            if i + 1 >= len(compressed_data):
                raise ValueError("Unexpected end of compressed data")
            
            byte = compressed_data[i + 1]
            decompressed.append(byte)
            
            # Update context
            context[context_index] = byte
            context_index = (context_index + 1) % context_size
            
            i += 2  # Skip flag and actual byte
        else:
            # Use predicted byte
            predicted = context[context_index]
            decompressed.append(predicted)
            
            # Update context
            context[context_index] = predicted
            context_index = (context_index + 1) % context_size
            
            i += 1
    
    return bytes(decompressed)