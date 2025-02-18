from collections import Counter
from typing import List, Dict, Tuple

def calculate_frequencies(data: str) -> Dict[str, int]:
    """
    Calculate the frequency of each character in the input data.
    
    :param data: Input string to analyze
    :return: Dictionary of character frequencies
    """
    return dict(Counter(data))

def sort_symbols_by_frequency(frequencies: Dict[str, int]) -> List[Tuple[str, int]]:
    """
    Sort symbols by their frequencies in descending order.
    
    :param frequencies: Dictionary of character frequencies
    :return: Sorted list of (symbol, frequency) tuples
    """
    return sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

def split_group(sorted_symbols: List[Tuple[str, int]]) -> Tuple[List[Tuple[str, int]], List[Tuple[str, int]]]:
    """
    Split the sorted symbols into two groups with minimal total frequency difference.
    
    :param sorted_symbols: List of (symbol, frequency) tuples sorted by frequency
    :return: Two groups of symbols
    """
    total_freq = sum(freq for _, freq in sorted_symbols)
    current_group_freq = 0
    min_diff = float('inf')
    split_index = 0

    for i in range(len(sorted_symbols)):
        current_group_freq += sorted_symbols[i][1]
        other_group_freq = total_freq - current_group_freq
        
        diff = abs(current_group_freq - other_group_freq)
        if diff < min_diff:
            min_diff = diff
            split_index = i + 1

    return sorted_symbols[:split_index], sorted_symbols[split_index:]

def generate_shannon_fano_codes(sorted_symbols: List[Tuple[str, int]], prefix: str = '') -> Dict[str, str]:
    """
    Recursively generate Shannon-Fano codes for symbols.
    
    :param sorted_symbols: List of (symbol, frequency) tuples sorted by frequency
    :param prefix: Current code prefix
    :return: Dictionary of symbol to code mappings
    """
    # Base case: single symbol
    if len(sorted_symbols) == 1:
        return {sorted_symbols[0][0]: prefix or '0'}
    
    # If two symbols, assign 0 and 1
    if len(sorted_symbols) == 2:
        return {
            sorted_symbols[0][0]: prefix + '0',
            sorted_symbols[1][0]: prefix + '1'
        }
    
    # Split the group and recursively generate codes
    group1, group2 = split_group(sorted_symbols)
    
    codes = {}
    codes.update(generate_shannon_fano_codes(group1, prefix + '0'))
    codes.update(generate_shannon_fano_codes(group2, prefix + '1'))
    
    return codes

def shannon_fano_encode(data: str) -> Tuple[Dict[str, str], str]:
    """
    Encode data using Shannon-Fano coding.
    
    :param data: Input string to encode
    :return: Tuple of code dictionary and encoded string
    """
    # Calculate frequencies
    frequencies = calculate_frequencies(data)
    
    # Sort symbols by frequency
    sorted_symbols = sort_symbols_by_frequency(frequencies)
    
    # Generate Shannon-Fano codes
    codes = generate_shannon_fano_codes(sorted_symbols)
    
    # Encode the data
    encoded_data = ''.join(codes[char] for char in data)
    
    return codes, encoded_data

def shannon_fano_decode(codes: Dict[str, str], encoded_data: str) -> str:
    """
    Decode data using Shannon-Fano codes.
    
    :param codes: Dictionary of symbol to code mappings
    :param encoded_data: Encoded binary string
    :return: Decoded original string
    """
    # Create reverse mapping of codes to symbols
    reverse_codes = {code: symbol for symbol, code in codes.items()}
    
    decoded_data = []
    current_code = ''
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = ''
    
    if current_code:
        raise ValueError("Invalid encoded data: incomplete code")
    
    return ''.join(decoded_data)