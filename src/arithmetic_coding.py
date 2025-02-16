from collections import Counter
from typing import List, Union, Dict

def arithmetic_encode(data: Union[str, List[str]]) -> Dict[str, float]:
    """
    Perform Arithmetic coding for data compression.
    
    Args:
        data (Union[str, List[str]]): Input data to be encoded
    
    Returns:
        Dict[str, float]: Dictionary containing probabilities and compressed value
    """
    # Convert input to list of characters if it's a string
    if isinstance(data, str):
        data = list(data)
    
    # Calculate frequency of each symbol
    freq_counter = Counter(data)
    total_symbols = len(data)
    
    # Calculate probabilities
    probabilities = {symbol: count/total_symbols for symbol, count in freq_counter.items()}
    
    # Sort symbols by their probability
    sorted_symbols = sorted(probabilities.keys(), key=lambda x: probabilities[x])
    
    # Initialize encoding range
    low, high = 0.0, 1.0
    
    # Arithmetic coding
    for symbol in data:
        range_width = high - low
        high = low + range_width * sum(probabilities[s] for s in sorted_symbols[:sorted_symbols.index(symbol)+1])
        low = low + range_width * sum(probabilities[s] for s in sorted_symbols[:sorted_symbols.index(symbol)])
    
    # Take the midpoint of the final range as the compressed value
    compressed_value = (low + high) / 2
    
    return {
        'probabilities': probabilities,
        'compressed_value': compressed_value
    }

def arithmetic_decode(compressed_info: Dict[str, float], original_length: int) -> List[str]:
    """
    Decode Arithmetic coded data.
    
    Args:
        compressed_info (Dict[str, float]): Compressed data information
        original_length (int): Length of the original data
    
    Returns:
        List[str]: Decoded data
    """
    probabilities = compressed_info['probabilities']
    compressed_value = compressed_info['compressed_value']
    
    # Sort symbols by their probability
    sorted_symbols = sorted(probabilities.keys(), key=lambda x: probabilities[x])
    
    # Initialize decoding
    decoded_data = []
    low, high = 0.0, 1.0
    
    # Decode symbols
    for _ in range(original_length):
        range_width = high - low
        
        # Find the symbol that contains the compressed value
        for symbol in sorted_symbols:
            symbol_high = low + range_width * sum(probabilities[s] for s in sorted_symbols[:sorted_symbols.index(symbol)+1])
            symbol_low = low + range_width * sum(probabilities[s] for s in sorted_symbols[:sorted_symbols.index(symbol)])
            
            if symbol_low <= compressed_value < symbol_high:
                decoded_data.append(symbol)
                low, high = symbol_low, symbol_high
                break
    
    return decoded_data