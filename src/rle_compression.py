def run_length_encode(data):
    """
    Implement Run-Length Encoding (RLE) for data compression.
    
    Args:
        data (str or list): Input data to be compressed
    
    Returns:
        list: Compressed data in the format [char, count]
    
    Raises:
        TypeError: If input is not a string or list
        ValueError: If input is an empty string or list
    """
    # Validate input
    if not isinstance(data, (str, list)):
        raise TypeError("Input must be a string or list")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    # Convert to list if string
    if isinstance(data, str):
        data = list(data)
    
    # Compression logic
    compressed = []
    if not data:
        return compressed
    
    current_char = data[0]
    current_count = 1
    
    for char in data[1:]:
        if char == current_char:
            current_count += 1
        else:
            compressed.append([current_char, current_count])
            current_char = char
            current_count = 1
    
    # Add the last group
    compressed.append([current_char, current_count])
    
    return compressed

def run_length_decode(compressed_data):
    """
    Decompress data that was compressed using Run-Length Encoding.
    
    Args:
        compressed_data (list): Compressed data in the format [char, count]
    
    Returns:
        list: Decompressed data
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input is malformed
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list")
    
    if not compressed_data:
        return []
    
    # Decompression logic
    decompressed = []
    
    for item in compressed_data:
        # Validate each compressed item
        if (not isinstance(item, list) or 
            len(item) != 2 or 
            not isinstance(item[0], (str, int)) or 
            not isinstance(item[1], int) or 
            item[1] < 1):
            raise ValueError("Malformed compressed data")
        
        char, count = item
        decompressed.extend([char] * count)
    
    return decompressed