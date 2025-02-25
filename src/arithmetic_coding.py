import math
from typing import List, Dict, Union


def arithmetic_encode(data: Union[str, List[str]], 
                      probability_model: Dict[str, float] = None) -> float:
    """
    Perform Arithmetic Encoding on input data.
    
    Args:
        data (Union[str, List[str]]): Input data to be encoded
        probability_model (Dict[str, float], optional): 
            Probability distribution of symbols. If None, 
            calculated from input data.
    
    Returns:
        float: Encoded value representing the compressed data
    
    Raises:
        ValueError: If input data is empty or probabilities are invalid
    """
    # Convert input to list of characters if it's a string
    if isinstance(data, str):
        data = list(data)
    
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Calculate probability model if not provided
    if probability_model is None:
        probability_model = calculate_probabilities(data)
    
    # Validate probability model
    validate_probability_model(probability_model)
    
    # Initialize encoding range
    low = 0.0
    high = 1.0
    
    # Perform encoding
    for symbol in data:
        # Calculate range width
        range_width = high - low
        
        # Calculate new bounds based on symbol probability
        symbol_prob = probability_model.get(symbol, 0)
        cumulative_prob = get_cumulative_prob(probability_model, symbol)
        
        # Update encoding range
        high = low + range_width * (cumulative_prob + symbol_prob)
        low = low + range_width * cumulative_prob
    
    # Return midpoint of final range as encoded value
    return (low + high) / 2


def arithmetic_decode(encoded_value: float, 
                      data_length: int, 
                      probability_model: Dict[str, float]) -> List[str]:
    """
    Perform Arithmetic Decoding to recover original data.
    
    Args:
        encoded_value (float): Compressed representation of data
        data_length (int): Length of original data
        probability_model (Dict[str, float]): 
            Probability distribution of symbols
    
    Returns:
        List[str]: Decoded data
    
    Raises:
        ValueError: If decoding is impossible
    """
    # Validate inputs
    validate_probability_model(probability_model)
    if data_length <= 0:
        raise ValueError("Data length must be positive")
    
    # Validate encoded value range
    if not (0 <= encoded_value <= 1):
        raise ValueError("Encoded value must be between 0 and 1")
    
    # Prepare for decoding
    decoded_data = []
    low = 0.0
    high = 1.0
    
    # Decode each symbol
    for _ in range(data_length):
        range_width = high - low
        
        # Find symbol that contains encoded value
        for symbol, prob in probability_model.items():
            cumulative_prob = get_cumulative_prob(probability_model, symbol)
            symbol_high = low + range_width * (cumulative_prob + prob)
            symbol_low = low + range_width * cumulative_prob
            
            if symbol_low <= encoded_value < symbol_high:
                decoded_data.append(symbol)
                
                # Update range for next symbol
                high = symbol_high
                low = symbol_low
                break
    
    return decoded_data


def calculate_probabilities(data: List[str]) -> Dict[str, float]:
    """
    Calculate symbol probabilities from input data.
    
    Args:
        data (List[str]): Input data
    
    Returns:
        Dict[str, float]: Probability distribution of symbols
    """
    if not data:
        raise ValueError("Cannot calculate probabilities for empty data")
    
    # Count symbol occurrences
    symbol_counts = {}
    for symbol in data:
        symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
    
    # Calculate probabilities
    total_symbols = len(data)
    return {symbol: count/total_symbols for symbol, count in symbol_counts.items()}


def validate_probability_model(model: Dict[str, float]) -> None:
    """
    Validate probability model.
    
    Args:
        model (Dict[str, float]): Probability distribution
    
    Raises:
        ValueError: If probabilities are invalid
    """
    if not model:
        raise ValueError("Probability model cannot be empty")
    
    total_prob = sum(model.values())
    if not math.isclose(total_prob, 1.0, rel_tol=1e-9):
        raise ValueError(f"Probabilities must sum to 1.0, got {total_prob}")
    
    if any(prob < 0 or prob > 1 for prob in model.values()):
        raise ValueError("Probabilities must be between 0 and 1")


def get_cumulative_prob(probability_model: Dict[str, float], 
                        symbol: str) -> float:
    """
    Calculate cumulative probability for a symbol.
    
    Args:
        probability_model (Dict[str, float]): Probability distribution
        symbol (str): Target symbol
    
    Returns:
        float: Cumulative probability of symbols before the target
    """
    return sum(prob for s, prob in probability_model.items() if s < symbol)