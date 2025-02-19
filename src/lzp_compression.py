def lzp_compress(data):
    """
    Implement LZP (Lempel-Ziv Prediction) compression algorithm.
    
    Args:
        data (bytes or str): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Initialize compression variables
    compressed = bytearray()
    context_bits = 8  # Size of context window
    context_mask = (1 << context_bits) - 1
    context = 0
    
    # Create prediction table
    prediction_table = [0] * 256
    
    # Compress data
    for byte in data:
        # Predict the next byte based on context
        predicted = prediction_table[context]
        
        if predicted == byte:
            # If prediction is correct, encode a match
            compressed.append(1)
        else:
            # If prediction is incorrect, encode the actual byte
            compressed.append(0)
            compressed.append(byte)
            
            # Update prediction table
            prediction_table[context] = byte
        
        # Update context (sliding window)
        context = ((context << 1) & context_mask) | (byte >> 7)
    
    return bytes(compressed)

def lzp_decompress(compressed_data):
    """
    Decompress data compressed with the LZP algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    # Initialize decompression variables
    decompressed = bytearray()
    context_bits = 8  # Size of context window
    context_mask = (1 << context_bits) - 1
    context = 0
    
    # Create prediction table
    prediction_table = [0] * 256
    
    # Iterate through compressed data
    i = 0
    while i < len(compressed_data):
        # Check prediction match flag
        if compressed_data[i] == 1:
            # Prediction matched, use predicted byte
            predicted = prediction_table[context]
            decompressed.append(predicted)
            
            # Update context and prediction table
            context = ((context << 1) & context_mask) | (predicted >> 7)
        else:
            # Prediction failed, read actual byte
            i += 1
            if i >= len(compressed_data):
                break
            
            byte = compressed_data[i]
            decompressed.append(byte)
            
            # Update prediction table
            prediction_table[context] = byte
            
            # Update context
            context = ((context << 1) & context_mask) | (byte >> 7)
        
        i += 1
    
    return bytes(decompressed)