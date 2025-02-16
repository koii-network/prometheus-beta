from typing import List, Dict, Union

def arithmetic_encode(message: str, probability_model: Dict[str, float] = None) -> float:
    """
    Perform Arithmetic Encoding for data compression.
    
    Args:
        message (str): The input string to be encoded
        probability_model (Dict[str, float], optional): Custom probability distribution. 
                      If not provided, will be calculated from the input message.
    
    Returns:
        float: The compressed representation of the input message
    
    Raises:
        ValueError: If probability model is invalid or message is empty
    """
    # Validate input
    if not message:
        raise ValueError("Message cannot be empty")
    
    # If no probability model is provided, create one from message
    if probability_model is None:
        probability_model = {}
        total_chars = len(message)
        for char in message:
            probability_model[char] = probability_model.get(char, 0) + 1 / total_chars
    
    # Validate probability model
    if not probability_model or abs(sum(probability_model.values()) - 1.0) > 1e-10:
        raise ValueError("Invalid probability model. Probabilities must sum to 1")
    
    # Sort characters by their probabilities for consistent encoding
    sorted_chars = sorted(probability_model.keys(), key=lambda x: probability_model[x])
    
    # Initialize encoding range
    low, high = 0.0, 1.0
    
    # Iteratively narrow the range for each character
    for char in message:
        range_width = high - low
        high = low + range_width * sum(probability_model[c] for c in sorted_chars if c <= char)
        low = low + range_width * sum(probability_model[c] for c in sorted_chars if c < char)
    
    # Return the midpoint of the final range as the encoded value
    return (low + high) / 2

def arithmetic_decode(encoded_value: float, 
                      message_length: int, 
                      probability_model: Dict[str, float]) -> str:
    """
    Perform Arithmetic Decoding to recover the original message.
    
    Args:
        encoded_value (float): The compressed representation
        message_length (int): Length of the original message
        probability_model (Dict[str, float]): Probability distribution of characters
    
    Returns:
        str: The decoded message
    
    Raises:
        ValueError: If input parameters are invalid
    """
    # Validate inputs
    if not (0 <= encoded_value <= 1):
        raise ValueError("Encoded value must be between 0 and 1")
    
    if message_length <= 0:
        raise ValueError("Message length must be positive")
    
    if not probability_model or abs(sum(probability_model.values()) - 1.0) > 1e-10:
        raise ValueError("Invalid probability model. Probabilities must sum to 1")
    
    # Sort characters by their probabilities for consistent decoding
    sorted_chars = sorted(probability_model.keys(), key=lambda x: probability_model[x])
    
    # Initialize decoding
    decoded_message = []
    current_value = encoded_value
    low, high = 0.0, 1.0
    
    # Decode each character
    for _ in range(message_length):
        range_width = high - low
        
        # Find the character for the current range
        for char in sorted_chars:
            new_low = low + range_width * sum(probability_model[c] for c in sorted_chars if c < char)
            new_high = low + range_width * sum(probability_model[c] for c in sorted_chars if c <= char)
            
            if new_low <= current_value < new_high:
                decoded_message.append(char)
                low, high = new_low, new_high
                break
    
    return ''.join(decoded_message)