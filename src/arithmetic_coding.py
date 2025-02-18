def arithmetic_encode(data):
    """
    Implement Arithmetic coding for data compression.
    
    Args:
        data (str): Input string to be compressed
    
    Returns:
        float: Compressed representation of the input data
    """
    # If input is empty, return 0.5 as a neutral value
    if not data:
        return 0.5
    
    # Calculate character probabilities
    char_count = {}
    total_chars = len(data)
    for char in data:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Sort characters by their frequency
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize interval
    low = 0.0
    high = 1.0
    
    # Compress the data
    for char in data:
        # Calculate the range
        range_width = high - low
        
        # Find the cumulative probability for this character
        cumulative_prob = 0
        for c, count in sorted_chars:
            if c == char:
                break
            cumulative_prob += count / total_chars
        
        # Update interval
        prob = char_count[char] / total_chars
        high = low + range_width * (cumulative_prob + prob)
        low = low + range_width * cumulative_prob
    
    # Return the midpoint of the final interval
    return (low + high) / 2

def arithmetic_decode(compressed_value, original_length, char_frequencies):
    """
    Decode an Arithmetic coded value back to the original string.
    
    Args:
        compressed_value (float): Compressed representation
        original_length (int): Length of the original string
        char_frequencies (dict): Frequency of characters in the original data
    
    Returns:
        str: Decoded string
    """
    # Validate inputs
    if not isinstance(compressed_value, (int, float)):
        raise ValueError("Compressed value must be a number")
    
    if compressed_value < 0 or compressed_value > 1:
        raise ValueError("Compressed value must be between 0 and 1")
    
    # Sort characters by their frequency
    sorted_chars = sorted(char_frequencies.items(), key=lambda x: x[1], reverse=True)
    total_chars = sum(char_frequencies.values())
    
    # Initialize decoding
    decoded = []
    low = 0.0
    high = 1.0
    
    for _ in range(original_length):
        # Calculate the range
        range_width = high - low
        
        # Find the character
        cumulative_prob = 0
        for char, count in sorted_chars:
            prob = count / total_chars
            new_high = low + range_width * (cumulative_prob + prob)
            
            if compressed_value >= low + range_width * cumulative_prob and \
               compressed_value < new_high:
                decoded.append(char)
                high = new_high
                low = low + range_width * cumulative_prob
                break
            
            cumulative_prob += prob
    
    return ''.join(decoded)