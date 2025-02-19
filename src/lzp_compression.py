def lzp_compress(data, context_size=8):
    """
    Implement Lempel-Ziv Prediction (LZP) compression algorithm.
    
    Args:
        data (bytes): Input data to compress
        context_size (int, optional): Size of the prediction context. Defaults to 8.
    
    Returns:
        bytes: Compressed data
    """
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if context_size < 1:
        raise ValueError("Context size must be at least 1")
    
    compressed = bytearray()
    context_buffer = bytearray(context_size)
    context_buffer_full = False
    
    for byte in data:
        # Check if context buffer is full
        if not context_buffer_full and len(context_buffer) == context_size:
            context_buffer_full = True
        
        # If context is full, try to predict the byte
        if context_buffer_full:
            # Simple prediction: look for recent context
            context = bytes(context_buffer)
            
            # If byte matches prediction, encode a short flag
            if byte == context[-1]:
                compressed.append(0)  # Prediction successful
            else:
                compressed.append(1)  # Prediction failed
                compressed.append(byte)
        else:
            # If context is not full, just append the byte
            compressed.append(byte)
        
        # Update context buffer
        context_buffer.append(byte)
        if len(context_buffer) > context_size:
            context_buffer.pop(0)
    
    return bytes(compressed)

def lzp_decompress(compressed, context_size=8):
    """
    Decompress data compressed with LZP algorithm.
    
    Args:
        compressed (bytes): Compressed input data
        context_size (int, optional): Size of the prediction context. Defaults to 8.
    
    Returns:
        bytes: Decompressed data
    """
    if not isinstance(compressed, bytes):
        raise TypeError("Input must be bytes")
    
    if context_size < 1:
        raise ValueError("Context size must be at least 1")
    
    decompressed = bytearray()
    context_buffer = bytearray(context_size)
    context_buffer_full = False
    
    i = 0
    while i < len(compressed):
        # Check if context buffer is full
        if not context_buffer_full and len(context_buffer) == context_size:
            context_buffer_full = True
        
        # If context is full, predict the byte
        if context_buffer_full:
            # Check prediction flag
            flag = compressed[i]
            i += 1
            
            if flag == 0:
                # Prediction successful, use last context byte
                byte = context_buffer[-1]
            else:
                # Prediction failed, use next byte
                byte = compressed[i]
                i += 1
            
            decompressed.append(byte)
        else:
            # If context is not full, just append the byte
            byte = compressed[i]
            decompressed.append(byte)
            i += 1
        
        # Update context buffer
        context_buffer.append(byte)
        if len(context_buffer) > context_size:
            context_buffer.pop(0)
    
    return bytes(decompressed)