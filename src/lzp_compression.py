def lzp_compress(data):
    """
    Implement LZP (Lempel-Ziv Prediction) compression algorithm.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        return b''
    
    # Initialize prediction dictionary
    pred_dict = {}
    compressed = bytearray()
    
    # Initial context is empty
    context = b''
    
    for byte in data:
        # Generate prediction key based on current context
        pred_key = context
        
        # Check if we have a prediction for this context
        if pred_key in pred_dict:
            predicted_byte = pred_dict[pred_key]
            
            # If the predicted byte matches the current byte
            if predicted_byte == byte:
                # Mark as a predicted byte (compression)
                compressed.append(0)
            else:
                # Encode the actual byte
                compressed.append(1)
                compressed.append(byte)
        else:
            # First time seeing this context, encode the byte
            compressed.append(1)
            compressed.append(byte)
        
        # Update prediction dictionary
        pred_dict[pred_key] = byte
        
        # Update context (slide the window)
        context = context[-3:] + bytes([byte])
    
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
    
    # Initialize prediction dictionary
    pred_dict = {}
    decompressed = bytearray()
    
    # Initial context is empty
    context = b''
    
    i = 0
    while i < len(compressed_data):
        # Check the prediction flag
        flag = compressed_data[i]
        i += 1
        
        # Generate prediction key based on current context
        pred_key = context
        
        if flag == 0:
            # Predicted byte - use dictionary prediction
            if pred_key in pred_dict:
                byte = pred_dict[pred_key]
            else:
                # If no prediction exists, this is an error
                raise ValueError("Compression error: No prediction for context")
        else:
            # Explicit byte encoding
            if i >= len(compressed_data):
                raise ValueError("Unexpected end of compressed data")
            byte = compressed_data[i]
            i += 1
        
        # Append the byte to decompressed data
        decompressed.append(byte)
        
        # Update prediction dictionary
        pred_dict[pred_key] = byte
        
        # Update context (slide the window)
        context = context[-3:] + bytes([byte])
    
    return bytes(decompressed)