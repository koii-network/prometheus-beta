def run_length_encode(data):
    """
    Perform Run-Length Encoding (RLE) compression on the input data.
    
    Args:
        data (str or list): The input data to compress
    
    Returns:
        list: Compressed data in the format [value, count]
    
    Raises:
        TypeError: If input is not a string or list
        ValueError: If input is an empty sequence
    """
    # Input validation
    if not data:
        raise ValueError("Input cannot be empty")
    
    if not isinstance(data, (str, list)):
        raise TypeError("Input must be a string or list")
    
    # Convert string to list if needed
    if isinstance(data, str):
        data = list(data)
    
    # Compression logic
    compressed = []
    current_value = data[0]
    current_count = 1
    
    for item in data[1:]:
        if item == current_value:
            current_count += 1
        else:
            compressed.append([current_value, current_count])
            current_value = item
            current_count = 1
    
    # Add the last run
    compressed.append([current_value, current_count])
    
    return compressed

def run_length_decode(compressed_data):
    """
    Decompress Run-Length Encoded data.
    
    Args:
        compressed_data (list): Compressed data in the format [value, count]
    
    Returns:
        list: Decompressed data
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input is invalid
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Decompression logic
    decompressed = []
    
    for item, count in compressed_data:
        if not isinstance(count, int) or count < 1:
            raise ValueError("Invalid compression format")
        decompressed.extend([item] * count)
    
    return decompressed