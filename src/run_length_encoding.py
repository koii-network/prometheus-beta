def compress_rle(data):
    """
    Implement Run-Length Encoding (RLE) compression.
    
    Args:
        data (str or list): Input data to compress
    
    Returns:
        str: Compressed representation of the input data
    
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
        return ''
    
    current = data[0]
    count = 1
    
    for item in data[1:]:
        if item == current:
            count += 1
        else:
            compressed.append(f"{count}{current}")
            current = item
            count = 1
    
    # Add the last run
    compressed.append(f"{count}{current}")
    
    return ''.join(compressed)

def decompress_rle(compressed_data):
    """
    Implement Run-Length Encoding (RLE) decompression.
    
    Args:
        compressed_data (str): Compressed data to decompress
    
    Returns:
        str: Decompressed original data
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is invalid or cannot be decompressed
    """
    # Validate input
    if not isinstance(compressed_data, str):
        raise TypeError("Input must be a string")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Decompression logic
    decompressed = []
    i = 0
    
    while i < len(compressed_data):
        # Extract count (potentially multi-digit)
        count_str = ''
        while i < len(compressed_data) and compressed_data[i].isdigit():
            count_str += compressed_data[i]
            i += 1
        
        # Validate count
        if not count_str:
            raise ValueError("Invalid compressed data format")
        
        count = int(count_str)
        
        # Get character
        if i >= len(compressed_data):
            raise ValueError("Invalid compressed data format")
        
        char = compressed_data[i]
        decompressed.extend([char] * count)
        
        i += 1
    
    return ''.join(decompressed)