from collections import Counter
from typing import Dict, List, Union

def shannon_fano_coding(data: Union[str, List[str]]) -> Dict[str, str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Args:
        data (str or List[str]): Input data to be encoded
    
    Returns:
        Dict[str, str]: A dictionary mapping original symbols to their compressed codes
    
    Raises:
        ValueError: If input data is empty
    """
    # Convert input to a single string if it's a list
    if isinstance(data, list):
        data = ''.join(data)
    
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Count frequency of each symbol
    freq = Counter(data)
    
    # Sort symbols by frequency in descending order
    sorted_symbols = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize coding dictionary
    codes = {}
    
    def generate_codes(symbols, current_code=''):
        """
        Recursively generate Shannon-Fano codes for a group of symbols
        
        Args:
            symbols (List): List of (symbol, frequency) tuples
            current_code (str): Current binary code prefix
        """
        if len(symbols) <= 1:
            # Base case: assign code to symbol
            if symbols:
                codes[symbols[0][0]] = current_code or '0'
            return
        
        # Find the splitting point that minimizes difference in total frequency
        total_freq = sum(freq for _, freq in symbols)
        current_freq = 0
        split_index = 0
        min_diff = float('inf')
        
        for i in range(len(symbols)):
            current_freq += symbols[i][1]
            diff = abs(current_freq - (total_freq - current_freq))
            
            if diff < min_diff:
                min_diff = diff
                split_index = i
        
        # Recursively generate codes for two groups
        generate_codes(symbols[:split_index+1], current_code + '0')
        generate_codes(symbols[split_index+1:], current_code + '1')
    
    # Generate codes
    generate_codes(sorted_symbols)
    
    return codes

def shannon_fano_encode(data: Union[str, List[str]], codes: Dict[str, str]) -> str:
    """
    Encode input data using pre-generated Shannon-Fano codes
    
    Args:
        data (str or List[str]): Input data to encode
        codes (Dict[str, str]): Shannon-Fano coding dictionary
    
    Returns:
        str: Encoded binary string
    """
    # Convert input to a single string if it's a list
    if isinstance(data, list):
        data = ''.join(data)
    
    # Encode each symbol
    return ''.join(codes[symbol] for symbol in data)

def shannon_fano_decode(encoded_data: str, codes: Dict[str, str]) -> str:
    """
    Decode Shannon-Fano encoded data
    
    Args:
        encoded_data (str): Binary encoded data
        codes (Dict[str, str]): Shannon-Fano coding dictionary
    
    Returns:
        str: Decoded original data
    """
    # Invert the codes dictionary for decoding
    reverse_codes = {code: symbol for symbol, code in codes.items()}
    
    decoded = []
    current_code = ''
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded.append(reverse_codes[current_code])
            current_code = ''
    
    # Check if all bits were decoded
    if current_code:
        raise ValueError("Invalid encoded data: Could not decode all bits")
    
    return ''.join(decoded)