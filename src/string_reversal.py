def reverse_string_in_place(s: str) -> str:
    """
    Reverse a string in-place without using extra memory.
    
    Args:
        s (str): Input string to be reversed.
    
    Returns:
        str: Reversed string.
    
    Note:
        In Python, strings are immutable, so we convert to list for in-place reversal.
    """
    # Convert string to list of characters for in-place manipulation
    chars = list(s)
    
    # Two-pointer approach to reverse the string
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters from both ends
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)