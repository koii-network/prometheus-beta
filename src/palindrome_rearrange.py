from collections import Counter

def can_form_palindrome(s: str) -> bool:
    """
    Determine if characters in the given string can be rearranged to form a palindrome.
    
    Args:
        s (str): Input string to check for palindrome rearrangement possibility
    
    Returns:
        bool: True if characters can be rearranged to form a palindrome, False otherwise
    """
    # Count the frequency of each character
    char_counts = Counter(s)
    
    # Count characters with odd frequencies
    odd_freq_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    
    # A string can be rearranged to a palindrome if at most one character has an odd frequency
    return odd_freq_count <= 1

def rearrange_to_palindrome(s: str) -> str:
    """
    Rearrange characters in the given string to form a palindrome.
    
    Args:
        s (str): Input string to rearrange
    
    Returns:
        str: A palindrome formed by rearranging characters, or an empty string if not possible
    """
    # First, check if a palindrome can be formed
    if not can_form_palindrome(s):
        return ""
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # Separate characters with odd and even frequencies
    odd_char = None
    even_chars = []
    
    for char, count in char_counts.items():
        if count % 2 == 0:
            even_chars.extend([char] * count)
        else:
            # If odd character exists, use it as the middle character
            if odd_char is None:
                odd_char = char
                even_chars.extend([char] * (count - 1))
            else:
                even_chars.extend([char] * (count - 1))
    
    # Construct palindrome
    half_length = len(even_chars) // 2
    left_half = sorted(even_chars[:half_length])
    right_half = sorted(even_chars[:half_length], reverse=True)
    
    if odd_char:
        return ''.join(left_half + [odd_char] + right_half)
    else:
        return ''.join(left_half + right_half)