from collections import Counter
from typing import List, Dict, Tuple

def shannon_fano_coding(data: str) -> Dict[str, str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Args:
        data (str): Input string to be encoded
    
    Returns:
        Dict[str, str]: Dictionary of character to binary code mappings
    
    Raises:
        ValueError: If input is empty
    """
    # Check for empty input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Count frequency of each character
    freq = Counter(data)
    
    # Sort characters by frequency in descending order
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Recursive function to generate Shannon-Fano codes
    def generate_codes(chars: List[Tuple[str, int]], code: str = '') -> Dict[str, str]:
        # Base case: if only one character left, assign current code
        if len(chars) == 1:
            return {chars[0][0]: code or '0'}
        
        # Find the split point to minimize variance
        total = sum(count for _, count in chars)
        cumulative = 0
        best_split = 0
        min_diff = float('inf')
        
        for i in range(len(chars)):
            cumulative += chars[i][1]
            diff = abs(2 * cumulative - total)
            if diff < min_diff:
                min_diff = diff
                best_split = i
        
        # Recursively generate codes for left and right groups
        left = chars[:best_split + 1]
        right = chars[best_split + 1:]
        
        left_codes = generate_codes(left, code + '0')
        right_codes = generate_codes(right, code + '1')
        
        # Merge the codes
        return {**left_codes, **right_codes}
    
    # Generate and return the Shannon-Fano codes
    return generate_codes(sorted_chars)

def shannon_fano_encode(data: str, codes: Dict[str, str]) -> str:
    """
    Encode the input data using pre-generated Shannon-Fano codes.
    
    Args:
        data (str): Input string to encode
        codes (Dict[str, str]): Shannon-Fano code mappings
    
    Returns:
        str: Encoded binary string
    """
    return ''.join(codes[char] for char in data)

def shannon_fano_decode(encoded: str, codes: Dict[str, str]) -> str:
    """
    Decode the encoded data using Shannon-Fano codes.
    
    Args:
        encoded (str): Binary encoded string
        codes (Dict[str, str]): Shannon-Fano code mappings
    
    Returns:
        str: Decoded original string
    """
    # Invert the codes dictionary for decoding
    inv_codes = {code: char for char, code in codes.items()}
    
    decoded = []
    current_code = ''
    
    for bit in encoded:
        current_code += bit
        if current_code in inv_codes:
            decoded.append(inv_codes[current_code])
            current_code = ''
    
    # Check if all bits were decoded
    if current_code:
        raise ValueError("Invalid encoded string")
    
    return ''.join(decoded)