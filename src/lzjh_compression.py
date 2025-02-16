def lzjh_compress(data):
    """
    Implement the LZJH (Lempel-Ziv-Jones-Hulme) compression algorithm.
    
    Args:
        data (bytes or str): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    """
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Initialize compression variables
    dictionary = {}
    result = bytearray()
    current_sequence = bytearray()
    next_code = 256
    
    for byte in data:
        # Extend current sequence
        current_sequence.append(byte)
        
        # If current sequence is not in dictionary, add it
        if bytes(current_sequence) not in dictionary:
            # If sequence has more than one byte, store previous code
            if len(current_sequence) > 1:
                result.extend(dictionary[bytes(current_sequence[:-1])])
            
            # Add new sequence to dictionary
            dictionary[bytes(current_sequence)] = (next_code).to_bytes(2, byteorder='big')
            next_code += 1
            
            # Reset current sequence to last byte
            current_sequence = bytearray([byte])
    
    # Add last sequence
    if current_sequence:
        if bytes(current_sequence) in dictionary:
            result.extend(dictionary[bytes(current_sequence)])
        else:
            result.extend(current_sequence)
    
    return bytes(result)

def lzjh_decompress(compressed_data):
    """
    Decompress data compressed with the LZJH algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    """
    # Initialize decompression variables
    dictionary = {i.to_bytes(1, byteorder='big'): i for i in range(256)}
    next_code = 256
    result = bytearray()
    current = None
    
    # Iterate through compressed data
    i = 0
    while i < len(compressed_data):
        # Try to read 2 bytes (compressed code)
        if i + 1 < len(compressed_data):
            code = int.from_bytes(compressed_data[i:i+2], byteorder='big')
            
            # Check if code is in dictionary
            if code in dictionary.values():
                entry = [k for k, v in dictionary.items() if v == code][0]
                result.extend(entry)
                
                # Add new dictionary entry
                if current is not None:
                    new_entry = current + entry[:1]
                    dictionary[bytes(new_entry)] = next_code
                    next_code += 1
                
                current = entry
                i += 2
            else:
                # If code not found, treat as single byte
                result.append(compressed_data[i])
                current = compressed_data[i:i+1]
                i += 1
        else:
            # Handle last byte
            result.append(compressed_data[i])
            i += 1
    
    return bytes(result)