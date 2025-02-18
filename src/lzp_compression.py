def lzp_compress(data):
    """
    Implement LZP (Lempel-Ziv Predictive) compression algorithm.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    """
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        return b''
    
    # Initialize compression parameters
    compressed = bytearray()
    context_size = 8  # Context length for prediction
    context_dict = {}
    current_context = b''
    
    for i in range(len(data)):
        # Update current context (sliding window)
        if len(current_context) > context_size:
            current_context = current_context[-context_size:]
        
        # Check if current context + next byte is in dictionary
        next_byte = bytes([data[i]])
        prediction_key = current_context + next_byte
        
        if prediction_key in context_dict:
            # If prediction is successful, encode a match
            compressed.append(1)  # Match flag
        else:
            # If no match, encode literal
            compressed.append(0)  # Literal flag
            compressed.append(data[i])
            
            # Update context dictionary
            context_dict[current_context + next_byte] = 1
        
        # Update current context
        current_context += next_byte
    
    return bytes(compressed)

def lzp_decompress(compressed):
    """
    Decompress data compressed with LZP algorithm.
    
    Args:
        compressed (bytes): Compressed data
    
    Returns:
        bytes: Decompressed data
    """
    if not isinstance(compressed, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed:
        return b''
    
    # Initialize decompression parameters
    decompressed = bytearray()
    context_size = 8  # Context length for prediction
    context_dict = {}
    current_context = b''
    
    i = 0
    while i < len(compressed):
        # Update current context (sliding window)
        if len(current_context) > context_size:
            current_context = current_context[-context_size:]
        
        # Check compression flag
        if compressed[i] == 0:  # Literal
            if i + 1 >= len(compressed):
                raise ValueError("Incomplete compressed data")
            
            literal = bytes([compressed[i + 1]])
            decompressed.extend(literal)
            
            # Update context dictionary
            context_dict[current_context + literal] = 1
            
            # Update current context
            current_context += literal
            i += 2
        elif compressed[i] == 1:  # Match
            # Predict next byte based on context
            # For simplicity, we'll use the last byte in the current context
            if current_context:
                predicted_byte = current_context[-1:]
            else:
                # If no context, use a default byte
                predicted_byte = b'\x00'
            
            decompressed.extend(predicted_byte)
            
            # Update context dictionary
            context_dict[current_context + predicted_byte] = 1
            
            # Update current context
            current_context += predicted_byte
            i += 1
        else:
            raise ValueError(f"Invalid compression flag: {compressed[i]}")
    
    return bytes(decompressed)