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
    result = []
    current_sequence = b''
    
    # LZH compression algorithm
    for byte in data:
        candidate = current_sequence + bytes([byte])
        
        if candidate in dictionary:
            current_sequence = candidate
        else:
            # Output the code for the existing sequence
            result.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary
            dictionary[candidate] = next_code
            next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Handle the last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    # Convert result to bytes
    return bytes(result)