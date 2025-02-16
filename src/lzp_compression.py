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
    
    compressed = bytearray()
    context_size = 4  # Context window size
    context_dict = {}
    
    # Initialize context with first few bytes
    current_context = data[:context_size]
    compressed.extend(current_context)
    
    i = context_size
    while i < len(data):
        # Look for matching context
        context = data[i-context_size:i]
        next_byte = data[i]
        
        # If context exists in dictionary, encode prediction
        if context in context_dict:
            predicted_byte = context_dict[context]
            
            # If prediction is correct, encode prediction flag
            if predicted_byte == next_byte:
                compressed.append(1)  # Prediction flag
            else:
                # Prediction failed, encode literal byte
                compressed.append(0)  # Literal flag
                compressed.append(next_byte)
                context_dict[context] = next_byte
        else:
            # New context, encode literal byte
            compressed.append(0)  # Literal flag
            compressed.append(next_byte)
            context_dict[context] = next_byte
        
        i += 1
    
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
    
    decompressed = bytearray()
    context_size = 4  # Match context window size
    context_dict = {}
    
    # Initialize context with first few bytes
    current_context = compressed_data[:context_size]
    decompressed.extend(current_context)
    
    i = context_size
    while i < len(compressed_data):
        context = decompressed[-context_size:]
        
        # Check prediction flag
        flag = compressed_data[i]
        i += 1
        
        if flag == 1:
            # Prediction successful
            if context in context_dict:
                next_byte = context_dict[context]
                decompressed.append(next_byte)
            else:
                # Context not found, treat as literal
                next_byte = compressed_data[i]
                i += 1
                decompressed.append(next_byte)
                context_dict[context] = next_byte
        else:
            # Literal byte
            next_byte = compressed_data[i]
            i += 1
            decompressed.append(next_byte)
            context_dict[context] = next_byte
    
    return bytes(decompressed)