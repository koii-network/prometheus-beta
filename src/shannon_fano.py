from collections import Counter
from typing import Dict, List, Tuple

def shannon_fano_coding(data: str) -> Dict[str, str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Args:
        data (str): Input string to be compressed
    
    Returns:
        Dict[str, str]: Dictionary mapping characters to their Shannon-Fano codes
    
    Raises:
        ValueError: If input is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Special case for single character
    if len(set(data)) == 1:
        return {data[0]: '0'}
    
    # Count character frequencies
    freq = Counter(data)
    
    # Sort characters by frequency in descending order
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Recursive function to generate Shannon-Fano codes
    def generate_codes(chars: List[Tuple[str, int]], code: str = '') -> Dict[str, str]:
        # Base case: single character
        if len(chars) <= 1:
            return {chars[0][0]: code} if chars else {}
        
        # Split the list into two groups with similar total frequencies
        total_freq = sum(freq for _, freq in chars)
        current_freq = 0
        split_index = 0
        min_diff = float('inf')
        
        for i in range(len(chars)):
            current_freq += chars[i][1]
            remaining_freq = total_freq - current_freq
            
            # Find the split point that minimizes the frequency difference
            diff = abs(current_freq - remaining_freq)
            if diff < min_diff:
                min_diff = diff
                split_index = i + 1
        
        # Recursive coding for two groups
        left_chars = chars[:split_index]
        right_chars = chars[split_index:]
        
        codes = {}
        # Add '0' to left group codes
        codes.update(generate_codes(left_chars, code + '0'))
        # Add '1' to right group codes
        codes.update(generate_codes(right_chars, code + '1'))
        
        return codes
    
    # Generate and return Shannon-Fano codes
    return generate_codes(sorted_chars)

def shannon_fano_encode(data: str, codes: Dict[str, str]) -> str:
    """
    Encode input data using Shannon-Fano codes.
    
    Args:
        data (str): Input string to encode
        codes (Dict[str, str]): Shannon-Fano coding dictionary
    
    Returns:
        str: Encoded binary string
    """
    return ''.join(codes[char] for char in data)

def shannon_fano_decode(encoded_data: str, codes: Dict[str, str]) -> str:
    """
    Decode Shannon-Fano encoded data.
    
    Args:
        encoded_data (str): Binary encoded string
        codes (Dict[str, str]): Shannon-Fano coding dictionary
    
    Returns:
        str: Decoded original string
    """
    # Invert the codes dictionary for decoding
    reverse_codes = {code: char for char, code in codes.items()}
    
    decoded = []
    current_code = ''
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded.append(reverse_codes[current_code])
            current_code = ''
    
    if current_code:
        raise ValueError("Invalid encoded data")
    
    return ''.join(decoded)