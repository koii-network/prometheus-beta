def run_length_encode(data):
    """
    Implement Run-Length Encoding (RLE) for data compression.
    
    Args:
        data (str or list): Input data to be compressed
    
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
    
    # Perform Run-Length Encoding
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