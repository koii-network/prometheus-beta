def run_length_encode(data):
    """
    Perform Run-Length Encoding (RLE) on the input data.
    
    Args:
        data (str or list): Input data to be compressed
    
    Returns:
        list: Compressed data in the format [char, count]
    
    Raises:
        TypeError: If input is not a string or list
        ValueError: If input is an empty string or list
    """
    # Input validation
    if not isinstance(data, (str, list)):
        raise TypeError("Input must be a string or list")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    # Convert to list if string
    if isinstance(data, str):
        data = list(data)
    
    # Run-Length Encoding
    compressed = []
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
    Decompress data encoded with Run-Length Encoding.
    
    Args:
        compressed_data (list): Compressed data in the format [char, count]
    
    Returns:
        list: Decompressed data
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input is empty or has invalid format
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Validate compressed data format
    for item in compressed_data:
        if not (isinstance(item, list) and len(item) == 2 and 
                isinstance(item[0], (str, int)) and 
                isinstance(item[1], int)):
            raise ValueError("Invalid compressed data format")
    
    # Decompression
    decompressed = []
    for char, count in compressed_data:
        decompressed.extend([char] * count)
    
    return decompressed