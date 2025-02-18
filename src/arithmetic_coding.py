def arithmetic_encode(data):
    """
    Implement Arithmetic coding for data compression.
    
    Args:
        data (str): Input string to be encoded
    
    Returns:
        float: Compressed representation of the input data
    """
    # If input is empty, return 0
    if not data:
        return 0.0
    
    # Calculate frequency of each character
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1
    
    # Normalize frequencies to probabilities
    total_chars = len(data)
    prob = {char: count/total_chars for char, count in freq.items()}
    
    # Sort characters by probability 
    sorted_chars = sorted(prob.keys(), key=lambda x: prob[x])
    
    # Initialize interval
    low, high = 0.0, 1.0
    
    # Encode each character
    for char in data:
        # Calculate range
        range_width = high - low
        
        # Update interval based on character probability
        characters = sorted_chars
        char_index = characters.index(char)
        cumulative_prob = sum(prob[c] for c in characters[:char_index])
        
        # Adjust interval
        high = low + range_width * (cumulative_prob + prob[char])
        low = low + range_width * cumulative_prob
    
    # Return the midpoint of final interval as compressed representation
    return (low + high) / 2

def arithmetic_decode(compressed_value, original_length, frequencies):
    """
    Decode the compressed value back to original data.
    
    Args:
        compressed_value (float): Compressed representation
        original_length (int): Length of original data
        frequencies (dict): Character frequencies
    
    Returns:
        str: Decoded original data
    """
    # Calculate probabilities
    total_chars = sum(frequencies.values())
    prob = {char: count/total_chars for char, count in frequencies.items()}
    
    # Sort characters by probability
    sorted_chars = sorted(prob.keys(), key=lambda x: prob[x])
    
    # Initialize decoding
    decoded = []
    low, high = 0.0, 1.0
    
    # Decode characters
    for _ in range(original_length):
        # Calculate range
        range_width = high - low
        
        # Find which character matches the compressed value
        for char in sorted_chars:
            # Calculate cumulative probability
            char_index = sorted_chars.index(char)
            cumulative_prob = sum(prob[c] for c in sorted_chars[:char_index])
            
            # Check if compressed value falls in this character's range
            char_low = low + range_width * cumulative_prob
            char_high = low + range_width * (cumulative_prob + prob[char])
            
            if char_low <= compressed_value < char_high:
                decoded.append(char)
                
                # Update interval
                high = char_high
                low = char_low
                break
    
    return ''.join(decoded)