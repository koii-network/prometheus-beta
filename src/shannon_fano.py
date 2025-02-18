from typing import Dict, List, Tuple

def shannon_fano_encode(data: str) -> Dict[str, str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Args:
        data (str): Input string to be compressed
    
    Returns:
        Dict[str, str]: Dictionary of characters to their Shannon-Fano codes
    """
    # Count frequency of each character
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1
    
    # Sort characters by frequency in descending order
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Recursive function to generate Shannon-Fano codes
    def generate_codes(chars: List[Tuple[str, int]], prefix: str = '') -> Dict[str, str]:
        if len(chars) <= 1:
            return {chars[0][0]: prefix} if chars else {}
        
        # Find the splitting point to minimize variance
        total = sum(char[1] for char in chars)
        current_sum = 0
        split_index = 0
        min_diff = float('inf')
        
        for i in range(len(chars)):
            current_sum += chars[i][1]
            group1_sum = current_sum
            group2_sum = total - group1_sum
            
            diff = abs(group1_sum - group2_sum)
            if diff < min_diff:
                min_diff = diff
                split_index = i
        
        # Recursively generate codes for each group
        left_group = chars[:split_index + 1]
        right_group = chars[split_index + 1:]
        
        codes = {}
        codes.update(generate_codes(left_group, prefix + '0'))
        codes.update(generate_codes(right_group, prefix + '1'))
        
        return codes
    
    # Generate and return Shannon-Fano codes
    return generate_codes(sorted_chars)

def shannon_fano_decode(codes: Dict[str, str], encoded_data: str) -> str:
    """
    Decode Shannon-Fano encoded data.
    
    Args:
        codes (Dict[str, str]): Shannon-Fano code mapping
        encoded_data (str): Compressed binary string
    
    Returns:
        str: Decoded original string
    """
    # Invert the codes dictionary
    reverse_codes = {code: char for char, code in codes.items()}
    
    decoded = []
    current_code = ''
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded.append(reverse_codes[current_code])
            current_code = ''
    
    if current_code:
        raise ValueError("Invalid encoded data: Incomplete code")
    
    return ''.join(decoded)