from collections import Counter
from typing import Dict, List, Tuple

def shannon_fano_coding(text: str) -> Dict[str, str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Args:
        text (str): Input text to be compressed
    
    Returns:
        Dict[str, str]: Dictionary mapping characters to their Shannon-Fano codes
    
    Raises:
        ValueError: If input text is empty
    """
    if not text:
        raise ValueError("Input text cannot be empty")
    
    # Count character frequencies
    freq = Counter(text)
    
    # Sort characters by frequency in descending order
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    def generate_codes(chars: List[Tuple[str, int]]) -> Dict[str, str]:
        """
        Recursively generate Shannon-Fano codes for a list of characters
        
        Args:
            chars (List[Tuple[str, int]]): List of (character, frequency) tuples
        
        Returns:
            Dict[str, str]: Dictionary of character codes
        """
        # Base case: single character
        if len(chars) <= 1:
            return {chars[0][0]: '0'} if chars else {}
        
        # Find the split point that minimizes difference in total frequency
        total_freq = sum(freq for _, freq in chars)
        left_freq = 0
        min_diff = float('inf')
        split_index = 0
        
        for i in range(len(chars)):
            left_freq += chars[i][1]
            right_freq = total_freq - left_freq
            diff = abs(left_freq - right_freq)
            
            if diff < min_diff:
                min_diff = diff
                split_index = i
        
        # Recursively generate codes for left and right groups
        left_chars = chars[:split_index + 1]
        right_chars = chars[split_index + 1:]
        
        left_codes = generate_codes(left_chars)
        right_codes = generate_codes(right_chars)
        
        # Prepend '0' to left codes, '1' to right codes
        for char in left_codes:
            left_codes[char] = '0' + left_codes[char]
        
        for char in right_codes:
            right_codes[char] = '1' + right_codes[char]
        
        # Merge and return codes
        return {**left_codes, **right_codes}
    
    # Generate and return Shannon-Fano codes
    return generate_codes(sorted_chars)

def encode_text(text: str, code_dict: Dict[str, str]) -> str:
    """
    Encode text using Shannon-Fano codes
    
    Args:
        text (str): Input text to encode
        code_dict (Dict[str, str]): Shannon-Fano code dictionary
    
    Returns:
        str: Encoded binary string
    
    Raises:
        ValueError: If any character is not in the code dictionary
    """
    try:
        return ''.join(code_dict[char] for char in text)
    except KeyError as e:
        raise ValueError(f"Character {e} not found in code dictionary")

def decode_text(encoded_text: str, code_dict: Dict[str, str]) -> str:
    """
    Decode text using Shannon-Fano codes
    
    Args:
        encoded_text (str): Binary encoded text
        code_dict (Dict[str, str]): Shannon-Fano code dictionary
    
    Returns:
        str: Decoded original text
    
    Raises:
        ValueError: If encoded text cannot be fully decoded
    """
    # Invert the code dictionary
    inv_code_dict = {code: char for char, code in code_dict.items()}
    
    decoded_text = []
    current_code = ''
    
    for bit in encoded_text:
        current_code += bit
        if current_code in inv_code_dict:
            decoded_text.append(inv_code_dict[current_code])
            current_code = ''
    
    # Check if all bits were decoded
    if current_code:
        raise ValueError("Unable to fully decode the encoded text")
    
    return ''.join(decoded_text)