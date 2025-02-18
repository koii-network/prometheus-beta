def run_length_encode(data):
    """
    Implements Run-Length Encoding (RLE) for data compression.
    
    Args:
        data (str or list): Input data to be compressed
    
    Returns:
        list: Compressed data in the format [char, count]
    
    Raises:
        TypeError: If input is not a string or list
        ValueError: If input is empty
    """
    # Input validation
    if not data:
        raise ValueError("Input cannot be empty")
    
    if not isinstance(data, (str, list)):
        raise TypeError("Input must be a string or list")
    
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
    
    # Add the last run
    compressed.append([current_char, current_count])
    
    return compressed