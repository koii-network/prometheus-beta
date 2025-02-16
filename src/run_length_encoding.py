def run_length_encode(data):
    """
    Perform Run-Length Encoding (RLE) on the input data.
    
    Args:
        data (str or list): Input data to be compressed
    
    Returns:
        list: Compressed data in the format of [char, count] pairs
    
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
    
    # Run-Length Encoding algorithm
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
    
    # Add the last run
    compressed.append([current_char, current_count])
    
    return compressed

def run_length_decode(compressed_data):
    """
    Decode Run-Length Encoded data back to its original form.
    
    Args:
        compressed_data (list): Compressed data in [char, count] format
    
    Returns:
        str: Decoded data
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input is invalid
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of [char, count] pairs")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Decode the compressed data
    decoded = []
    for item in compressed_data:
        if not isinstance(item, list) or len(item) != 2:
            raise ValueError("Each item must be a [char, count] pair")
        
        char, count = item
        if not isinstance(count, int) or count < 1:
            raise ValueError("Count must be a positive integer")
        
        decoded.extend([char] * count)
    
    return ''.join(decoded)