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
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    
    # Can form palindrome if at most one character has an odd frequency
    return odd_count <= 1

def rearrange_to_palindrome(s: str) -> str:
    """
    Rearrange characters in the string to form a palindrome.
    
    Args:
        s (str): Input string to rearrange
    
    Returns:
        str: Palindrome formed from input characters, or empty string if not possible
    """
    # Check if palindrome rearrangement is possible
    if not can_form_palindrome(s):
        return ""
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # Separate characters with even and odd frequencies
    even_chars = [char * (count // 2) for char, count in char_counts.items() if count % 2 == 0]
    odd_chars = [char for char, count in char_counts.items() if count % 2 != 0]
    
    # Construct palindrome
    left_half = ''.join(sorted(even_chars + (odd_chars[0:1] if odd_chars else [])))
    right_half = left_half[::-1]
    
    # Combine left and right halves
    return left_half + right_half