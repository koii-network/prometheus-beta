import typing

def lzh_compress(data: typing.Union[str, bytes]) -> bytes:
    """
    Implement LZH (Lempel-Ziv-Huffman) compression algorithm.
    
    Args:
        data (str or bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not str or bytes
        ValueError: If input is empty
    """
    # Input validation
    if data is None:
        raise TypeError("Input must be str or bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")
    
    # Convert to bytes if input is a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Initialize compression dictionary and variables
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    result_codes = []
    current_sequence = b''
    
    # LZH compression algorithm
    for byte in data:
        candidate = current_sequence + bytes([byte])
        
        if candidate in dictionary:
            current_sequence = candidate
        else:
            # Output the code for the existing sequence
            if current_sequence:
                result_codes.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary
            dictionary[candidate] = next_code
            next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Handle the last sequence
    if current_sequence:
        result_codes.append(dictionary[current_sequence])
    
    # Convert result codes to a compact byte representation
    def encode_compressed_data(codes):
        max_code_length = len(bin(max(codes))) - 2  # Determine max bit length
        compact_bytes = bytearray()
        
        # Store the max code length as the first byte
        compact_bytes.append(max_code_length)
        
        # Pack the codes
        bit_buffer = 0
        bit_count = 0
        for code in codes:
            bit_buffer = (bit_buffer << max_code_length) | code
            bit_count += max_code_length
            
            while bit_count >= 8:
                compact_bytes.append(bit_buffer >> (bit_count - 8))
                bit_buffer &= ((1 << (bit_count - 8)) - 1)
                bit_count -= 8
        
        # Handle any remaining bits
        if bit_count > 0:
            compact_bytes.append(bit_buffer << (8 - bit_count))
        
        return bytes(compact_bytes)
    
    return encode_compressed_data(result_codes)