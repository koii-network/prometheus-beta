from typing import List, Dict, Tuple

def arithmetic_encode(data: str) -> Tuple[float, Dict[str, float]]:
    """
    Perform arithmetic encoding for data compression.
    
    Args:
        data (str): Input string to be compressed
    
    Returns:
        Tuple[float, Dict[str, float]]: 
        - Compressed value (a float between 0 and 1)
        - Probability distribution of characters
    """
    # If input is empty, return 0.5 and empty distribution
    if not data:
        return 0.5, {}
    
    # Calculate character frequencies
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1
    
    # Calculate probability distribution
    total_chars = len(data)
    prob_dist = {char: count/total_chars for char, count in freq.items()}
    
    # Sort characters by their cumulative probability
    sorted_chars = sorted(prob_dist.keys(), key=lambda x: prob_dist[x])
    
    # Initialize interval
    low, high = 0.0, 1.0
    
    # Iterate through each character in the input
    for char in data:
        # Calculate the range for this character
        range_width = high - low
        high = low + range_width * sum(prob_dist[c] for c in sorted_chars if c <= char)
        low = low + range_width * sum(prob_dist[c] for c in sorted_chars if c < char)
    
    # Return the midpoint of the final interval
    compressed_value = (low + high) / 2
    
    return compressed_value, prob_dist

def arithmetic_decode(compressed_value: float, 
                      prob_dist: Dict[str, float], 
                      length: int) -> str:
    """
    Decode a previously arithmetically encoded message.
    
    Args:
        compressed_value (float): The compressed value
        prob_dist (Dict[str, float]): Probability distribution of characters
        length (int): Original message length
    
    Returns:
        str: Decoded message
    """
    # Validate inputs
    if not (0 <= compressed_value <= 1):
        raise ValueError("Compressed value must be between 0 and 1")
    
    if not prob_dist:
        raise ValueError("Probability distribution cannot be empty")
    
    # Sort characters by their probabilities
    sorted_chars = sorted(prob_dist.keys(), key=lambda x: prob_dist[x])
    
    # Initialize decoding interval
    low, high = 0.0, 1.0
    decoded_message = []
    
    # Decode for the specified length
    for _ in range(length):
        # Find the character whose subinterval contains the compressed value
        for char in sorted_chars:
            range_width = high - low
            char_low = low + range_width * sum(prob_dist[c] for c in sorted_chars if c < char)
            char_high = low + range_width * sum(prob_dist[c] for c in sorted_chars if c <= char)
            
            if char_low <= compressed_value < char_high:
                decoded_message.append(char)
                low, high = char_low, char_high
                break
    
    return ''.join(decoded_message)