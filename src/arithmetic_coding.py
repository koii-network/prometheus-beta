import math
from typing import List, Dict, Union

def arithmetic_encode(data: Union[str, List[str]], probability_model: Dict[str, float] = None) -> float:
    """
    Perform Arithmetic Encoding for data compression.
    
    Args:
        data (Union[str, List[str]]): Input data to be encoded
        probability_model (Dict[str, float], optional): Pre-defined probability distribution. 
                                                       If None, calculates from input data.
    
    Returns:
        float: Compressed representation of the input data
    
    Raises:
        ValueError: If input data is empty or probabilities are invalid
    """
    # Convert input to list if it's a string
    if isinstance(data, str):
        data = list(data)
    
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # If no probability model is provided, calculate from input
    if probability_model is None:
        probability_model = {}
        total_count = len(data)
        for symbol in data:
            probability_model[symbol] = probability_model.get(symbol, 0) + 1 / total_count
    
    # Validate probability model sum
    prob_sum = sum(probability_model.values())
    if not math.isclose(prob_sum, 1.0, rel_tol=1e-9):
        raise ValueError(f"Probabilities must sum to 1.0 (current sum: {prob_sum})")
    
    # Validate all symbols from data exist in probability model
    data_symbols = set(data)
    prob_symbols = set(probability_model.keys())
    if not data_symbols.issubset(prob_symbols):
        missing_symbols = data_symbols - prob_symbols
        raise ValueError(f"Missing probability for symbols: {missing_symbols}")
    
    # Sort symbols by cumulative probability
    sorted_symbols = sorted(probability_model.items(), key=lambda x: x[1])
    cumulative_probs = [0.0]
    for _, prob in sorted_symbols:
        cumulative_probs.append(cumulative_probs[-1] + prob)
    
    # Initialize encoding range
    low, high = 0.0, 1.0
    
    # Encode each symbol
    for symbol in data:
        # Find symbol's range
        symbol_index = next(i for i, (sym, _) in enumerate(sorted_symbols) if sym == symbol)
        
        # Update encoding range
        range_width = high - low
        high = low + range_width * cumulative_probs[symbol_index + 1]
        low = low + range_width * cumulative_probs[symbol_index]
    
    # Return the midpoint of the final range as the encoded value
    return (low + high) / 2.0

def arithmetic_decode(encoded_value: float, data_length: int, probability_model: Dict[str, float]) -> List[str]:
    """
    Perform Arithmetic Decoding to recover original data.
    
    Args:
        encoded_value (float): Compressed representation
        data_length (int): Length of original data
        probability_model (Dict[str, float]): Probability distribution of symbols
    
    Returns:
        List[str]: Decoded data
    
    Raises:
        ValueError: If inputs are invalid
    """
    # Validate inputs
    if data_length <= 0:
        raise ValueError("Data length must be positive")
    
    # Validate probability model sum
    prob_sum = sum(probability_model.values())
    if not math.isclose(prob_sum, 1.0, rel_tol=1e-9):
        raise ValueError(f"Probabilities must sum to 1.0 (current sum: {prob_sum})")
    
    # Sort symbols by cumulative probability
    sorted_symbols = sorted(probability_model.items(), key=lambda x: x[1])
    cumulative_probs = [0.0]
    for _, prob in sorted_symbols:
        cumulative_probs.append(cumulative_probs[-1] + prob)
    
    # Decoded data list
    decoded_data = []
    
    # Current position in the encoded value
    current = encoded_value
    
    # Decode symbols
    for _ in range(data_length):
        # Find which symbol the current value corresponds to
        for i in range(len(sorted_symbols)):
            if cumulative_probs[i] <= current < cumulative_probs[i+1]:
                # Add the symbol to decoded data
                decoded_data.append(sorted_symbols[i][0])
                
                # Update current value
                current = (current - cumulative_probs[i]) / (cumulative_probs[i+1] - cumulative_probs[i])
                break
    
    return decoded_data