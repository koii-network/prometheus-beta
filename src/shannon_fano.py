from collections import Counter
from typing import List, Dict, Union

def shannon_fano_coding(data: Union[str, List[str]]) -> Dict[str, str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Args:
        data (str or List[str]): Input data to be encoded
    
    Returns:
        Dict[str, str]: Dictionary mapping original symbols to their encoded bit strings
    
    Raises:
        ValueError: If input data is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert input to list if it's a string
    if isinstance(data, str):
        data = list(data)
    
    # Calculate frequency of each symbol
    freq = Counter(data)
    
    # Sort symbols by frequency in descending order
    sorted_symbols = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    
    # Recursive function to generate Shannon-Fano codes
    def generate_codes(symbols):
        # Base case: single symbol
        if len(symbols) <= 1:
            return {symbols[0]: '0'} if symbols else {}
        
        # Find the split point to minimize variance
        total_freq = sum(freq[sym] for sym in symbols)
        current_sum = 0
        split_index = 0
        min_diff = float('inf')
        
        for i in range(len(symbols)):
            current_sum += freq[symbols[i]]
            left_sum = current_sum
            right_sum = total_freq - left_sum
            
            # Find the split point that minimizes the difference between left and right groups
            if abs(left_sum - right_sum) < min_diff:
                min_diff = abs(left_sum - right_sum)
                split_index = i
        
        # Recursively generate codes for left and right groups
        left_group = symbols[:split_index + 1]
        right_group = symbols[split_index + 1:]
        
        left_codes = generate_codes(left_group)
        right_codes = generate_codes(right_group)
        
        # Prepend '0' to left group codes, '1' to right group codes
        for sym in left_codes:
            left_codes[sym] = '0' + left_codes[sym]
        for sym in right_codes:
            right_codes[sym] = '1' + right_codes[sym]
        
        # Merge and return codes
        return {**left_codes, **right_codes}
    
    # Generate and return Shannon-Fano codes
    return generate_codes(sorted_symbols)

def encode_data(data: Union[str, List[str]], codes: Dict[str, str]) -> str:
    """
    Encode input data using provided Shannon-Fano codes.
    
    Args:
        data (str or List[str]): Input data to encode
        codes (Dict[str, str]): Shannon-Fano encoding dictionary
    
    Returns:
        str: Encoded bit string
    
    Raises:
        ValueError: If input data contains symbols not in codes
    """
    # Convert input to list if it's a string
    if isinstance(data, str):
        data = list(data)
    
    # Validate all symbols have codes
    if not all(sym in codes for sym in data):
        raise ValueError("Input contains symbols not in the encoding dictionary")
    
    # Encode each symbol
    return ''.join(codes[sym] for sym in data)

def decode_data(encoded_data: str, codes: Dict[str, str]) -> str:
    """
    Decode Shannon-Fano encoded data.
    
    Args:
        encoded_data (str): Bit string to decode
        codes (Dict[str, str]): Shannon-Fano encoding dictionary
    
    Returns:
        str: Decoded original data
    
    Raises:
        ValueError: If encoded data cannot be decoded
    """
    # Create reverse mapping
    reverse_codes = {code: sym for sym, code in codes.items()}
    
    decoded = []
    current_code = ''
    
    for bit in encoded_data:
        current_code += bit
        
        # Check if current code matches any encoded symbol
        if current_code in reverse_codes:
            decoded.append(reverse_codes[current_code])
            current_code = ''
    
    # Ensure entire encoded data was decoded
    if current_code:
        raise ValueError("Unable to decode entire input")
    
    return ''.join(decoded)